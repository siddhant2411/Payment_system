var prodcutDeatilsAPI= 'http://127.0.0.1:5000/productDetails'
$(function () {
        
      

    $.get(prodcutDeatilsAPI, function (response) {
        if(response) {
            var table = '';
           
             $.each(response, function(index,response) {
                table += '<tr>'+
                    '<td>'+ response.pid+'</td>'+
                    '<td>'+ response.name+'</td>'+
                    '<td>'+ response.price+'</td>'+
                    '<td>'+ response.quantity +'</td>'+
                    '<td>'+ response.unit_name +'</td></tr>'
                    
                    console.log(response);
                    console.log(response.name);
                    
             });
        } 
        $("table").find('tbody').empty().html(table);
       // $("#new-order-id").find('tbody').html(table);
    });
    
});
