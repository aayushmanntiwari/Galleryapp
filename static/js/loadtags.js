$(window).on('load',function(e){
    e.preventDefault();
    $.ajax({
    type:'GET',
    /* if no error will be found then this url will be run successfully*/
    url:'/ajax/load-tags/',
    data_type:'html',
    success:function (data){
        console.log("success");
        /* this will basically show all the tags without page load*/
        $('#selettag').html(data.rendered_table);
    },

    });
});