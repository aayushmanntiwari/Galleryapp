/*$(document).ready(function(){*/
    $(document).on('click','.filter-checkbox',function(){
        var _filterObj = {};
        $('.filter-checkbox').each(function(name,ele){
            var _filterval = $(this).val();
            var _filterkey = $(this).data('filter');
            /* This will store those value who are checked*/
            _filterObj[_filterkey]=Array.from(document.querySelectorAll('input[data-filter='+ _filterkey+']:checked')).map(function(el){
                return el.value;
           });
        });
        //run ajax
        $.ajax({
            url:'/filter-data',
            data:_filterObj,
            data_type:'html',
            beforeSend:function(){
                $("#image-cards").html('');
                $('#loader').removeClass("hide");
                $('#pagination').addClass('hide');
            },
            success:function(res) {
                $("#image-cards").html(res.rendered_table);
                $('#loader').addClass("hide");
                $('#pagination').removeClass("hide");
            }
        });
    });

/*});*/