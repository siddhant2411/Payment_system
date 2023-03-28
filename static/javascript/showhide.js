var insertOrderAPI = 'http://127.0.0.1:5000/insertOrder';
var barcodeNumberAPI = 'http://127.0.0.1:5000/scan';
var orderSaveApiUrl = 'http://127.0.0.1:5000/saveOrder';

var showQRCode='http://127.0.0.1:5000/hello';
function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        data: data
    }).done(function (msg) {
        window.location.reload();
    });
}

sum = 0;

count=0

$("#add-more-items-order").click(function () {
    
    addItem(count)
    count++;
});

function addItem(count) {
   
    $.get(insertOrderAPI, function (response) {

        if (response) {
            
            var table = '';
            console.log(response);
            $.each(response, function (index, response) {
                
                response.total = parseInt(response.price) * parseInt(response.quantity)
                productname = response.name.replaceAll(/\s/g, '')
                console.log(productname)
                table += '<tr>' +
                    '<td><input readonly="readonly" name="Product_name" class="input-value" id="new-order-name"  value=' + productname + '></input></td>' +
                    '<td><input readonly="readonly" name="Product_price" class="input-value" id="new-order-price'+count+'" value =' + response.price + '></input></td>' +
                    '<td><input  name="Product_quantity" class="input-value" id="qty'+count+'" onchange="call(this,'+count+')" value =' + response.quantity + '></input></td>' +
                    '<td><input readonly="readonly" name="Product_unit" class="input-value" id="new-order-unit" value =' + response.unit_name + '></input></td>' +
                    '<td><input readonly="readonly" name="Product_total" class="input-value" id="new-order-total'+count+'" value =' + response.total + '></input></td>'+
                    '<td style="display:none;"><input readonly="readonly"  name="pid" class="input-value"  value ='+response.pid+'></input></td></tr>';


                 
                console.log(response);
                console.log(response.pid)
                sum = sum + response.total
                console.log("COunt is "+count)


            })
            $("table").find('tbody').append(table);
        }

        console.log(sum)
        document.getElementById("product_grand_total").value = sum
    });

}


$("#saveOrder").on("click", function () {
    if(document.getElementById("mobile-no").value.length <= 0)
    {
        alert("Please Input valid phone number")
        return false
    }
    else
    {
        var formData = $("form").serializeArray();
        var requestPayload = {
            mobile_no: null,
            amount: null,
            payment_type: null,
            // total: null,
            order_details: []
        };
        var orderDetails = [];
        for (var i = 0; i < formData.length; ++i) {
            var element = formData[i];
            var lastElement = null;

            switch (element.name) {
                case 'mobile_no':
                    requestPayload.mobile_no = element.value;
                    console.log(element.name)
                    break;
                case 'product_grand_total':
                    requestPayload.amount = element.value;
                    console.log(requestPayload.amount)
                    break;
                case 'payment_type':
                    requestPayload.payment_type = element.value;
                    console.log(requestPayload.payment_type)
                    break;
                case 'Product_name':
                    requestPayload.order_details.push({
                        Product_name: element.value,
                        Product_price: null,
                        Product_quantity: null,
                        Product_unit: null,
                        Product_total: null,
                        pid: null

                    });
                    console.log(element.name)
                    break;
                case 'Product_price':
                    lastElement = requestPayload.order_details[requestPayload.order_details.length - 1];
                    lastElement.Product_price = element.value
                    console.log(element.name)
                case 'Product_quantity':
                    lastElement = requestPayload.order_details[requestPayload.order_details.length - 1];
                    lastElement.Product_quantity = element.value
                    console.log(element.name)
                    break;
                case 'Product_unit':
                    lastElement = requestPayload.order_details[requestPayload.order_details.length - 1];
                    lastElement.Product_unit = element.value
                    console.log(element.name)
                case 'Product_total':
                    lastElement = requestPayload.order_details[requestPayload.order_details.length - 1];
                    lastElement.Product_total = element.value
                    console.log(element.name)
                    break;
                case 'pid':
                    lastElement = requestPayload.order_details[requestPayload.order_details.length - 1];
                    lastElement.pid= element.value
                    console.log(element.name)
                    break;
            }

        }
        callApi("POST", orderSaveApiUrl, {
            'data': JSON.stringify(requestPayload)
        });
        window.location.href = "QRCode.html";

    }
        
});




/*$(function () {
  
    $.get(orderSaveApiUrl, function (response) {
        if(response) {
            var table = '';
           
            
                table += '<tr>' +
                    '<td>'+ response.name+'</td>'+
                    '<td>'+ response.price+'</td>'+
                    '<td>'+ response.quantity +'</td>'+
                    '<td>'+ response.unit +'</td>'+
                    '<td>'+ response.total +'</td></tr>';
                    console.log(response);
                    console.log(response.name)
            
           
           
        } $("table").find('tbody').empty().html(table);
    });
});*/

function call(index,count)
{
    var price= document.getElementById("new-order-price"+count).value
    console.log(price)
    // console.log(index.value)

    var qty= document.getElementById("qty"+count).value
    console.log(qty)

    var Item_select = document.getElementById("new-order-total"+count)
    old_item_total = Item_select.value

    new_item_total= price*qty

    Item_select.value= new_item_total

    grand_total= document.getElementById("product_grand_total")
  
    sum= grand_total.value-old_item_total+new_item_total
    grand_total.value = grand_total.value-old_item_total+new_item_total

    console.log(sum)
    
    // var b= document.getElementById("new-order-quantity").value
    // console.log(ans)
    
}

function required()
{
    if(document.getElementById("mobile-no").value.length <= 0)
    {
        alert("Please Input valid phone number")
    }
    
}