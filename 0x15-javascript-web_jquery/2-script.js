// updates the text color of the header element to red 
// when user clicks on the tag DIV#red_header

$(function()
{
    $('DIV#red_header').attr("onclick", "$('DIV#red_header').css('color', 'red')")
});