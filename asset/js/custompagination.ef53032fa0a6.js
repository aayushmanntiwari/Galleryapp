$(document).ready(function(){
    var items = $('#image-cards #items');
    var numItems = items.length;
    var perPage = 8;
    items.slice(perPage).hide();
    $('#pagination-container').pagination({
        items: numItems, 
        itemsOnPage:perPage,  
        currentPage: 1,
        prevText: "Prev", 
        nextText: "Next", 
        cssStyle: "light-theme", 
        onPageClick :function(pageNumber){
            var showFrom = perPage * (pageNumber - 1);
            var showTo = showFrom + perPage;
            items.hide().slice(showFrom,showTo).show();
        }
    });
});