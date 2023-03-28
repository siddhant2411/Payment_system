var productSaveApiUrl = 'http://127.0.0.1:5000/insertProduct';
var barcodeNumberAPI = 'http://127.0.0.1:5000/scan';



function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        data: data
    }).done(function( msg ) {
        window.location.reload();
    });
}
$("#start-scanner").click(function () {
 
    scanBarcode()
});

function scanBarcode()
{
    $.get(barcodeNumberAPI,function(number){
        if(number) {
            
            console.log(number.pid)
            document.getElementById("add-product-id").value =number.pid;    
            document.getElementById("add-product-name").value =number.name;       
            console.log(number.pid)
        }
    });
}

$("#save-product").click(function () {
   
    var data = $("#productForm").serializeArray();
    var requestPayload = {
        pid: null,
        name: null,
        price: null,
        quantity: null,
        unit:null
    };
    for (var i=0;i<data.length;++i) {
        var element = data[i];
        switch(element.name) {
            case 'pid':
                requestPayload.pid = element.value;
                break;
            case 'name':
                requestPayload.name = element.value;
                break;
            case 'price':
                requestPayload.price = element.value;
                break;
            case 'quantity':
                requestPayload.quantity=element.value;
            case 'unit':
                    requestPayload.unit=element.value;
        }
    }
    console.log(requestPayload)
    callApi("POST", productSaveApiUrl, {'data': JSON.stringify(requestPayload)
    });
});


