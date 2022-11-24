// updates the text of the <header> element to New Header!!!
// when user clicks on DIV#update_header

$(function()
{
    $('DIV#update_header').attr("onclick", '$("header").text("New Header!!!")');
});