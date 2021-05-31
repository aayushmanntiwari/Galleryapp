function buildList(tags){
    var wrapper = document.getElementById('image-cards')
    console.log(tags)
    if (wrapper!= null){
        var url = '/ajax/load-images/' + tags
        fetch(url)
		.then((resp) => resp.json())
		.then(function(data){
            var state = document.readyState
            if (state == 'interactive') {
                $('#loader').removeClass("hide");
                if (wrapper!= null){
                    wrapper.html('');
                }
            }
            else { 
                $('#loader').addClass("hide");
                if (wrapper!= null){
                    wrapper.innerHTML = ""
                }
                var list = data
                for (var i in list){
                    if(list[i].image_url_as_list!=''){
                        var img = `<img src="${list[i].image_url_as_list}" class="image-thumbail" style="width:100%"><br><br>`
                    }
                    else if (list[i].image_image_url_as_list!='') {
                        var img = `<img src="${list[i].image_image_url_as_list}" class="image-thumbail" style="width:100%"><br><br>`
                    }
                    if (list[i].image_url_as_list!=""){
                        var download_img = `<a id="${list[i].id}" href="${list[i].image_url_as_list}" download><i class="fa fa-download fa-lg"></i></a>`
                    }
                    else if (list[i].image_image_url_as_list!="") {
                        var download_img = `<a id="${list[i].id}" href="${list[i].image_image_url_as_list}" download><i class="fa fa-download fa-lg"></i></a>`
                    }
                    var item = `
                    <div class="col-md-4 col-6 p-2" id="items">
                        <div class="card">
                            ${img}
                            <div class="card-body">
                                <div style="display: flex; justify-content: center;">
                                    <div class="fixed">
                                        <button type="button" class="btn btn-primary btn-md m-2" data-toggle="modal" data-item-id="${list[i].id}" data-target="#exampleModalshowimmagedata_${list[i].id}">
                                            info  
                                        </button> 
                                    </div>
                                    <div class="fixed pt-3 pl-3">
                                        ${download_img}
                                    </div>                                                     
                                </div>
                                
                            </div>
                            <!-- Model to show single image details -->
                            <div class="modal fade" id="exampleModalshowimmagedata_${list[i].id}" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
                                <div class="modal-dialog modal-dialog-centered" role="document">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalLongTitle">${list[i].title}</h5>
                                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                            <span aria-hidden="true">&times;</span>
                                        </button>
                                    </div>
                                        <div class="d-flex justify-content-center pt-2 hide" id="loader-two-${list[i].id}">
                                            <div class="spinner-border" role="status">
                                            <span class="sr-only">Loading...</span>
                                            </div>
                                        </div>
                                        <div class="modal-body modal-body-${list[i].id}">
                                            
                                                <div class="container" id="item-${list[i].id}">
                                                    ${img}
                                                    <p>Rotate Image</p>
                                                    <a class="clockwisebutton-filter btn-primary p-2 "  data-href="/rotateimage/modal-body-${list[i].id}/${list[i].id}/-90/" model-id="${list[i].id}" data-item-id="${list[i].id}" data-clockwise-id="-90">Clockwise</a>
                                                    <a class="Anticlockwisebutton-filter btn-primary p-2" data-href="/rotateimage/modal-body-${list[i].id}/${list[i].id}/90/" model-id="${list[i].id}" data-item-id="${list[i].id}" data-clockwise-id="90">AntiClockwise</a>
                                                </div>
                                        </div>
                                        
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                        </div>
                                </div>
                                </div>
                            </div>
                            <!--./ Model to show single image details -->
                        </div>
                    </div>`
                    if (wrapper!= null){
                        wrapper.innerHTML += item
                    }
                }
                return;
            }
        });

    }

};
