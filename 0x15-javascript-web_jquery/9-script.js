// fetches from a URL and displays the value of hello from an HTML tag

$(document).ready(function () {
    $.ajax({
        type: 'GET',
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        success: function(data){
           $('DIV#hello').append(data.hello);
        }
    });
});
