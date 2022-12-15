// fetches the character name from a URL using JQuery API
url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
$(function() {
    $.get(url, (data, textStatus)=>{
        $('DIV#character').text(data['name']);
    });
});