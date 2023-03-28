var orderDeatilsAPI = 'http://127.0.0.1:5000/orderDetails';

$(function () {
        
      

    $.get(orderDeatilsAPI, function (response) {
        if(response) {
            var table = '';
           
             $.each(response, function(index,response) {
                table += '<tr>' +
                    '<td >'+ response.order_id+'</td>'+
                    '<td>'+ response.date+'</td>'+
                    '<td>'+ response.mobile_no+'</td>'+
                    '<td>'+ response.amount +'</td>'+
                    '<td>'+ response.payment_name +'</td></tr>';
                    console.log(response);
                    console.log(response.date);
                    
             });
        } 
        $("table").find('tbody').empty().html(table);
       // $("#new-order-id").find('tbody').html(table);
    });
    
});

