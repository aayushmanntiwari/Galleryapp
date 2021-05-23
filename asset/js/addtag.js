$(document).ready(function(){
    var form = document.getElementById('tag-form')
    if (form!=null) {
    form.addEventListener('submit', function(e){
        console.log('Form submitted')
        var url = '/api/addtag/'
        var tag_name = document.getElementById('tag-name').value;
        fetch(url, {
            method:'POST',
            headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'name':tag_name,})
        }
        ).then(function(response){
        /* this will reset the form*/
        document.tag-form.reset();
        $("#addtag").modal('hide')
        return false;
        })
    })
    }
});