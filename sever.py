from werkzeug.utils import redirect

import ScanAndName
from flask import Flask, request, jsonify, url_for, render_template, Response
import json
import BarcodeScan
import cv2
import requests
from bs4 import BeautifulSoup
from pyzbar import pyzbar
from sql_connection import get_sql_connection
import data_access



app = Flask(__name__)
connection = get_sql_connection()

@app.route('/scan', methods=['GET'])
def scan():
    ScanAndName.main()
    ans = jsonify({
        "pid":ScanAndName.barcode_value,
        "name":ScanAndName.product_name
    })
    ScanAndName.stop=0
    ans.headers.add('Access-Control-Allow-Origin', '*')
    return ans

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return "Hello"

@app.route('/productDetails')
def getProductDetails():
    response=data_access.get_products(connection)
    response=jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/manage_products')
def manage_products():
    return render_template("manage-products.html")

@app.route('/add_product')
def add_product():
    return render_template("Add-product.html")

@app.route('/insertProduct' ,methods=['POST'])
def insertNewProduct():
    request_payload = json.loads(request.form['data'])
    pid= data_access.insert_new_product(connection, request_payload)
    response = jsonify({
        'pid': pid
    })
    print(pid)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertOrder')
def scanNumber():
    BarcodeScan.main()
    BarcodeScan.stop=0
    ans= BarcodeScan.barcode_value
    print("Barcode is done",ans)
    response=data_access.get_products_order(connection,ans)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/neworder')
def neworder():
    return render_template("neworder.html")

@app.route('/saveOrder' ,methods=['POST'])
def saveOrder():
    request_payload = json.loads(request.form['data'])
    print("request payload")
    print(request_payload)
    products_info=[]
    for title, value in request_payload.items():
        print(title)
        print(type(value))
        if(type(value)==list):
            for i in value:
                if i != None:
                    products_info.append(i)
    # print("Done iteration")
    # print(products_info)
    order_id = data_access.insert_order(connection, request_payload)
    print(order_id)
    data_access.order_details(connection,products_info,order_id)

    response = jsonify({
        'order_id': order_id
    })

    print("This is it",request_payload)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/orderDetails')
def getOrderDetails():
    response=data_access.get_orders(connection)
    response=jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')

    return response


@app.route('/deleteProducts',methods=['POST'] )
def deleteProducts():
    return_id = data_access.delete_product(connection, request.form['pid'])
    response = jsonify({
       'pid': return_id
    })
    print("This is it",response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    userId = request.form.get("userId")
    password = request.form.get('password')

    # response= jsonify({'userId':userId,'password':password})
    print(userId, password)
    ans = data_access.login_info(connection,userId, password)

    print(ans)

    # response.headers.add('Access-Control-Allow-Origin', '*')
    if ans:
        # return render_template("fetch_enq.html")
        # global LogedInUser
        # LogedInUser = username
        return redirect(url_for('home'))
    else:
        return render_template("loginPage.html")

@app.route('/', methods=['GET', 'POST'])
def index():
    # userId = request.form.get("userId")
    # print(userId)

    return render_template("loginPage.html")

@app.route('/home', methods=['GET', 'POST'])
def home():
    # userId = request.form.get("userId")
    # print(userId)

    return render_template("index.html")

@app.route("/display_products")
def display_products():
    return render_template("display-products.html")

@app.route("/display_orders")
def display_orders():
    return render_template("display-orders.html")

@app.route("/orderitems")
def order_items():
    oid=46
    response = data_access.order_items(connection,oid)
    # response=jsonify(response)
    print(response)
    return render_template("order-items.html",data=response)

@app.route("/pdf")
def genrate_pdf():
    oid=46
    result =data_access.order_items(connection, oid)
    pdf = FPDF()
    pdf.add_page()
    #
    page_width = pdf.w - 2 * pdf.l_margin
    #
    # pdf.set_font('Times', 'B', 14.0)
    # pdf.cell(page_width, 0.0, 'Employee Data', align='C')
    # pdf.ln(10)

    pdf.set_font('Courier', '', 12)

    col_width = page_width / 4

    pdf.ln(1)

    th = pdf.font_size

    for row in result:
        pdf.cell(col_width, th, str(row[0])[1:-1], ln=1,align='l')

        pdf.cell(col_width, th,"",  ln=1,align='l')
        pdf.cell(140, th, "Product Name",align='l')
        pdf.cell(5, th, "Unit", align='l')
        pdf.cell(5, th, "Price", align='l')

        pdf.cell(col_width, th, "", ln=3, align='l')
        pdf.cell(140, th, str(row[1][0][1]),align='l')
        pdf.cell(5, th, str(row[1][0][2]),  align='l')
        pdf.cell(5, th, str(row[1][0][3]),  align='l')
        # pdf.cell(col_width, th, row[3], border=1)

        pdf.ln(th)

    pdf.ln(10)

    pdf.set_font('Times', '', 10.0)
    pdf.cell(page_width, 0.0, '- end of report -', align='C')
    pdf.output("GFG.pdf")
    return redirect("/orderitems")

@app.route("/QRCode")
def QRCode():
    return render_template("QRCode.html")
if __name__ ==  "__main__":
    print("Starting python flask")
    app.run(port=5000)
