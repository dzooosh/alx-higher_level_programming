// adds a <li> element to a list

$(function()
{
   $("DIV#add_item").attr("onclick", '$("UL.my_list").append("<li>Item</li>")');
});