// switch between two classes of the header element

$(function()
{
    $("DIV#toggle_header").attr("onclick", "$('header').toggleClass('green red')");
});