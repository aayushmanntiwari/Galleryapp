$(document).on('click','.clockwisebutton-filter',function(e){
    var direction_val = $(this).attr("data-clockwise-id");
    var id =  $(this).attr("data-item-id");
    var tags = $(this).attr("data-tags");
    $.ajax(
        {
            type:"GET",
            url: "/rotateimage/",
            data:{
                direction_val: direction_val,
                id:id,
                tags:tags,
            },
            data_type:'html',
            headers:{
                'Content-type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            success:function(data) 
            {
                $('#image-cards').html(data.rendered_table);
                /*document.getElementsByClassName('modal-backdrop')[0].style.display = "none";
                document.getElementsByTagName('html')[0].style.overflow = "auto";
                document.getElementsByClassName('modal-backdrop')[0].style.opacity=0;*/
            }
         });
});



$(document).on('click','.Anticlockwisebutton-filter',function(e){
    var direction_val = $(this).attr("data-clockwise-id");
    var id =  $(this).attr("data-item-id");
    var tags = $(this).attr("data-tags");
    $.ajax(
        {
            type:"GET",
            url: "/rotateimage/",
            data:{
                direction_val: direction_val,
                id:id,
                tags:tags,
            },
            data_type:'html',
            headers:{
                'Content-type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            success:function(data) 
            {
                $('#image-cards').html(data.rendered_table);
                /*document.getElementsByClassName('modal-backdrop')[0].style.display = "none";
                document.getElementsByTagName('html')[0].style.overflow = "auto";
                document.getElementsByClassName('modal-backdrop')[0].style.opacity=0;*/
                
            }
         });
});