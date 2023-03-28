from datetime import datetime, date

# import mysql.connector
from sql_connection import get_sql_connection
def get_products(connection):
    cursor =connection.cursor()

    #query = ("SELECT products.pid, products.name, products.price, products.quantity, products.unit,unit_identifire.unit_name FROM ssip.products inner join unit_identifire on unit_identifire.unit_id=products.unit")
    query= "SELECT products.pid, products.name, products.price, products.quantity, products.unit,unit_identifire.unit_name from products inner join unit_identifire on unit_identifire.unit_id=products.unit"

    cursor.execute(query)
    response=[]
    for (pid, name, price, quantity, unit, unit_name) in cursor:
      response.append({'pid':pid,
                       'name':name,
                       'price':price,
                       'quantity':quantity,
                       'unit_name':unit_name
                       })
    return response
def insert_new_product(connection,product):
    cursor = connection.cursor()

    query = "INSERT INTO products (pid, name, price,quantity,unit) VALUES ('%s','%s',%s,%s,%s)"%(product['pid'],product['name'],float(product['price']),float(product['quantity']),int(product['unit']))
    #data=(int(product['pid']),product['name'],float(product['price']),int(product['quantity']),int(product['unit']))

    print(query)
    print("this",query)
    cursor.execute(query)
    connection.commit()
    print(cursor.rowcount, "record(s) inserted")

def delete_product(connection,pid):
    cursor = connection.cursor()

    query = (
        "DELETE FROM products WHERE pid="+str(pid))
    cursor.execute(query)
    connection.commit()
    #return cursor.lastrowid
    print(cursor.rowcount, "record(s) deleted")

def get_orders(connection):
    cursor =connection.cursor()

   # query = ("SELECT order.order_id, order.date, order.mobile_no, order.amount, payment_method.payment_name FROM ssip.order inner join ssip.payment_method on ssip.order.payment_type=ssip.payment_method.payment_type order by order_id desc")
    query="SELECT orders.order_id, orders.date, orders.mobile_no, orders.amount, payment_method.payment_name FROM orders inner join payment_method on orders.payment_type=payment_method.payment_type order by order_id desc LIMIT 10"

    cursor.execute(query)
    response=[]
    for (order_id, date,mobile_no, amount,payment_name) in cursor:
      response.append({'order_id':order_id,
                       'date':str(date),
                       'mobile_no':mobile_no,
                       'amount':amount,
                       'payment_name':payment_name
                       })

    return response

def insert_order(connection,order):
    cursor = connection.cursor()

   # query = "INSERT INTO ssip.order (date,mobile_no,amount,payment_type) VALUES (%s, %s, %s, %s)"

    query= "INSERT INTO orders (date,mobile_no,amount,payment_type) VALUES ('%s', %s,%s,%s)"%(date.today(),int(order['mobile_no']), int(order['amount']),int(order['payment_type']))
    print(query)
   # data = (datetime.today(),int(order['mobile_no']), int(order['amount']),int(order['payment_type']) )

    cursor.execute(query)
    query = "select orders.Order_id from orders ORDER BY Order_id DESC LIMIT 1"
    cursor.execute(query)

    for Order_id in cursor:
       order_id= Order_id
    order_id= int(order_id[0])
    connection.commit()
    return order_id
def get_products_order(connection,barcode_no):
    cursor =connection.cursor()

    #query = ("SELECT products.name, products.price, products.quantity, products.unit,unit_identifire.unit_name FROM  ssip.products  inner join unit_identifire on unit_identifire.unit_id=products.unit where pid="+str(barcode_no))
    query=("SELECT products.name, products.price, products.quantity, products.unit,unit_identifire.unit_name FROM  products  inner join unit_identifire on unit_identifire.unit_id=products.unit where pid="+str(barcode_no))
    cursor.execute(query)
    response = []
    for(name,price,quantity,unit,unit_name) in cursor:
     response.append({ 'name':name,
                       'price':price,
                       'quantity':quantity,
                       'unit_name':unit_name,
                       'pid': barcode_no
                       })
    print("function",response)
    return response
if __name__ == '__main__':
    connection=get_sql_connection()
    delete_product(connection, 2)
    '''insert_new_product(connection,{
          'pid': '33',
          'name': 'x',
          'price': '200',
          'quantity': '8',
          'unit': '1'
      })'''
    #abc=get_products_order(connection,16)
    #print(abc)
   # print(get_products(connection))
def login_info(connection,userId, password):
    # connection = get_sql_connection()
    cursor = connection.cursor()
    query = "select user_login.user_name,user_login.password from user_login where user_name='" + userId + "'"
    print(query)
    cursor.execute(query)
    result = cursor.fetchall()
    print(len(result))
    print(cursor)
    flag = 0
    User_Name = ""
    if cursor.rowcount == 0:
        message = ("Invalid User")
    else:
        for (user_Name,Password) in result:
            # print(User_Id)
            if (password == Password):
                message = ("Welcome")
                flag = 1
            else:
                message = ("invalid Password")

    return (flag)


def order_details(connection, products_info,order_id):
    cursor = connection.cursor()
    for item in products_info:
        query = "INSERT INTO Order_product (Order_id,product_name,product_unit,product_price,product_quntity,product_total,pid) VALUES (%s,'%s','%s',%s,%s,%s,'%s')"%(order_id, item['Product_name'],item['Product_unit'],float(item['Product_price']),int(item['Product_quantity']), float(item['Product_total']),item['pid'])
        print(query)
        cursor.execute(query)
        connection.commit()
    # return None


def order_items(connection, oid):
    cursor = connection.cursor()
    query="SELECT orders.order_id, orders.date, orders.mobile_no, orders.amount, payment_method.payment_name FROM orders  inner join payment_method on orders.payment_type=payment_method.payment_type where order_id= %s"%(oid)

    print(query)
    cursor.execute(query)
    response=[]
    # for (order_id, date,mobile_no, amount,payment_name) in cursor:
    #  # response.append({'order_id':order_id,
    #  #                  'date':str(date),
    #  #                  'mobile_no':mobile_no,
    #  #                  'amount':amount,
    #  #                  'payment_name':payment_name
    #  #                  })
    #     response.append(order_id,date,mobile_no,amount,payment_name)
    details= cursor.fetchone()
    query="select * from Order_product where Order_id=%s"%oid
    cursor.execute(query)
    # for (order_id, product_name, product_unit, product_price,product_quntity, product_total,pid) in cursor:
    #     response.append({
    #         'product_Name':product_name,
    #         'product_unit':product_unit,
    #         'product_price':product_price,
    #         'product_quntity':product_quntity,
    #         'product_total':product_total,
    #         'pid':pid
    #     })
    response.append((details,cursor.fetchall()))
    return response
