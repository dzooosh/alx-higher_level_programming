// fetches and lists the title for all movies
url = "https://swapi-api.alx-tools.com/api/films/?format=json";

$(function()
{
    $.get(url, (data, textStatus)=>
    {
        data['results'].forEach(function(item) {
            $('UL#list_movies').append($("<li>"+item['title']+"</li>"));
        });
    });
});