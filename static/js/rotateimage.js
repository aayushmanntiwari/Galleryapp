$(document).on('click','.clockwisebutton-filter',function(e){
    var direction_val = $(this).attr("data-clockwise-id");
    var id =  $(this).attr("data-item-id");
    var model_id =  $(this).attr("model-id");
    var dataURL = $(this).attr('data-href');
    $.ajax(
        {
            type:"POST",
            /*url: "/rotateimage/",*/
            data:{
                direction_val: direction_val,
                id:id,
                model_id:model_id,
            },
            data_type:'html',
            headers:{
                'Content-type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            success:function(data) 
            {
                $('.modal-body-'+String(model_id)).load(dataURL,function(){
                    $('#exampleModalshowimmagedata_'+String(model_id)).modal('hide');
                });
                $('body').removeClass().removeAttr('style');$('.modal-backdrop').remove();
            }
         });
});



$(document).on('click','.Anticlockwisebutton-filter',function(e){
    var direction_val = $(this).attr("data-clockwise-id");
    var id =  $(this).attr("data-item-id");
    var model_id =  $(this).attr("model-id");
    var dataURL = $(this).attr('data-href');
    $.ajax(
        {
            type:"GET",
            data:{
                direction_val: direction_val,
                id:id,
            },
            data_type:'html',
            headers:{
                'Content-type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            success:function(data) 
            {
                $('.modal-body-'+String(model_id)).load(dataURL,function(){
                    $('#exampleModalshowimmagedata_'+String(model_id)).modal('hide');
                });
                $('body').removeClass().removeAttr('style');$('.modal-backdrop').remove();            
            }
         });
});