// form upload
$(window).on('load',function(e){
    $.ajax({
    type:'GET',
    /* if no error will be found then this url will be run successfully*/
    url:'/ajax/all/filter/tags/',
    data_type:'html',
    success:function (data){
            console.log("success");
            /* this will basically show all the tags without page load*/
            $('#filter-tags').html(data.rendered_table);
        },
        });
    });
    // end