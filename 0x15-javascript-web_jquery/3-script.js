// changes header to red
// when user clicks on div#red_header

$(function()
{
    $("DIV#red_header").attr("onclick", "$('header').addClass('red')");
});