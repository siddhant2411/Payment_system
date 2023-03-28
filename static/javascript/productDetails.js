var prodcutDeatilsAPI = 'http://127.0.0.1:5000/productDetails';
var barcodeNumberAPI = 'http://127.0.0.1:5000/scan';
var productDeleteAPI = 'http://127.0.0.1:5000/deleteProducts';


function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        data: data
    }).done(function( msg ) {
        window.location.reload();
    });
}

$(function () {
        
      
    
    $.get(prodcutDeatilsAPI, function (response) {
        console.log(response)
        if(response) {
            var table = '';
           
             $.each(response, function(index,response) {
                table += '<tr  data-id="'+ response.pid +'" data-name="'+ response.name +'" data-price="'+ response.price+'"data-quantity="'+response.quantity+'"data-unit="'+response.name+'">'+
                    '<td id="product-id">'+ response.pid+'</td>'+
                    '<td>'+ response.name+'</td>'+
                    '<td>'+ response.price+'</td>'+
                    '<td>'+ response.quantity +'</td>'+
                    '<td>'+ response.unit_name +'</td>'+
                    '<td><button class="delete-product">Delete</button></td></tr>'
                    console.log(response);
                    console.log(response.name);
                    
             });
        } 
        $("table").find('tbody').empty().html(table);
    //    $(".order-details-box").find('tbody').append().html(table);
    });
    
});

$(document).on("click", ".delete-product", function (){
    var tr = $(this).closest('tr');
    var data = {
        pid : tr.data('id'),
        
    };
    console.log(data)
    var isDelete = confirm("Are you sure to delete "+ tr.data('name') +" item?");
    if (isDelete) {
        callApi("POST", productDeleteAPI, data);
    }
});
