$(document).on('click','.clockwisebutton-filter',function(e){
    var direction_val = $(this).attr("data-clockwise-id");
    var id =  $(this).attr("data-item-id");
    var model_id =  $(this).attr("model-id");
    var dataURL = $(this).attr('data-href');
    var tags = $(this).attr('data-filter-tags');
    $.ajax(
        {
            type:"GET",
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
            beforeSend:function(){
                $('#loader-two-'+String(model_id)).removeClass("hide");
            },
            success:function(data) 
            {
                $('.modal-body-'+String(model_id)).load(dataURL,function(){
                    $('#exampleModalshowimmagedata_'+String(model_id)).modal('hide');
                    buildList(tags);
                });
                $('#loader-two-'+String(model_id)).addClass("hide");
                $('body').removeClass().removeAttr('style');$('.modal-backdrop').remove();
            }
         });
});



$(document).on('click','.Anticlockwisebutton-filter',function(e){
    var direction_val = $(this).attr("data-clockwise-id");
    var id =  $(this).attr("data-item-id");
    var model_id =  $(this).attr("model-id");
    var dataURL = $(this).attr('data-href');
    var tags = $(this).attr('data-filter-tags');
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
            beforeSend:function(){
                $('#loader-two-'+String(model_id)).removeClass("hide");
            },
            success:function(data) 
            {
                $('.modal-body-'+String(model_id)).load(dataURL,function(){
                    $('#exampleModalshowimmagedata_'+String(model_id)).modal('hide');
                    buildList(tags);
                });
                $('#loader-two-'+String(model_id)).addClass("hide");
                $('body').removeClass().removeAttr('style');$('.modal-backdrop').remove();           
            }
         });
});