var insertOrderAPI = 'http://127.0.0.1:5000/insertOrder';
var barcodeNumberAPI = 'http://127.0.0.1:5000/scan';
var orderSaveApiUrl = 'http://127.0.0.1:5000/saveOrder';


function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        data: data
    }).done(function( msg ) {
       window.location.reload();
    });
}

sum=0;
/*$('.add-new-product').click(function()
{
    
    scan_barcode()
   
    

    //sum= sum + last_value;
    //console.log(sum);
    //datatosend = 'this is my matrix';
    //result = runPyScript(datatosend);
    //console.log('Got back ' + result);
    
});
 /*function runPyScript(input){
        var jqXHR = $.ajax({
            type: "POST",
            url: "D:/sid/study/SSIP%20project/Coding/html/testing.py",
            async: false,
            data: { mydata: input }
        });

        return jqXHR.responseText;
    }
*/


$("#add-more-items-order").click(function () {
 
    addItem()
   
});

function addItem()
{
    $.get(insertOrderAPI, function (response) 
    {
        
        if(response) 
        {
            var table = '';
      
            $.each(response, function(index,response) {
                     response.total=parseInt(response.price)*parseInt(response.quantity)
                     productname=response.name.replaceAll(/\s/g,'')
                     console.log(productname)
                     table += '<tr>' +
                    '<td><input readonly="readonly" name="Product_name" class="input-value" id="new-order-name"  value='+productname+'></input></td>'+
                    '<td><input readonly="readonly" name="Product_price" class="input-value" id="new-order-price" value ='+response.price+'></input></td>'+
                    '<td><input  name="Product_quantity" class="input-value" id="new-order-quantity" value ='+response.quantity+'></input></td>'+
                    '<td><input readonly="readonly" name="Product_unit" class="input-value" id="new-order-unit" value ='+response.unit_name+'></input></td>' +
                    '<td><input readonly="readonly" name="Product_total" class="input-value" id="new-order-total" value ='+response.total+'></input></td></tr>';

                  
                   
                    console.log(response); 
                    console.log(response.pid)
                    sum=sum+response.total
                  
                    
            })
            $("table").find('tbody').append(table); 
        }   
       
        console.log(sum)
    document.getElementById("product_grand_total").value=sum
    });
    
}
      
  
$("#saveOrder").on("click", function(){
    var formData = $("form").serializeArray();
    var requestPayload = {
        mobile_no: null,
        amount:null,
        payment_type:null
       // total: null,
        //order_details: []
    };
    var orderDetails = [];
    for(var i=0;i<formData.length;++i) {
        var element = formData[i];
        var lastElement = null;
        
        switch(element.name) {
            case 'mobile_no':
                requestPayload.mobile_no = element.value;
                console.log(element.name)
                break;
            case 'product_grand_total':
                requestPayload.amount = element.value;
                console.log(requestPayload.amount)
                break;
            case 'payment_type':
                requestPayload.payment_type=element.value;
                console.log(requestPayload.payment_type)
                break;
            /*case 'Product_name':
                requestPayload.order_details.push({
                    Product_name: element.value,
                    Product_price: null,
                    Product_quantity: null,
                    Product_unit:null,
                    Product_total: null
                    
                });    
                console.log(element.name)            
                break;
            case 'Product_price':
                    lastElement = requestPayload.order_details[requestPayload.order_details.length-1];
                    lastElement.Product_price = element.value
                    console.log(element.name)
            case 'Product_quantity':
                lastElement = requestPayload.order_details[requestPayload.order_details.length-1];
                lastElement.Product_quantity = element.value
                console.log(element.name)
                break;
            case 'Product_unit':
                    lastElement = requestPayload.order_details[requestPayload.order_details.length-1];
                    lastElement.Product_unit = element.value
                    console.log(element.name)
            case 'Product_total':
                lastElement = requestPayload.order_details[requestPayload.order_details.length-1];
                lastElement.Product_total = element.value
                console.log(element.name)
                break;*/
        }

    }
    callApi("POST", orderSaveApiUrl, {
        'data': JSON.stringify(requestPayload)
    });
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