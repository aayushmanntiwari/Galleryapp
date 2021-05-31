import io
import cloudinary
import requests
import ast
from io import StringIO
from django.http.response import HttpResponse, JsonResponse
import mimetypes
from PIL import Image as PilImage
from django.core import serializers
from django.shortcuts import render,redirect
from .models import Images
from taggit.models import Tag
from rest_framework import status
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template.loader import render_to_string
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger 
from .serializers import TagsSerializers,ImagesSerializers
from .forms import ImageFileUploadForm
from django.core.files.base import ContentFile


# Create your views here.
@api_view(['GET','POST'])
def home(request):
    images = Images.objects.all()
    return render(request,'index.html',{'images':images})



@api_view(['POST'])
def addimage(request):
    data = request.POST
    images = request.FILES.getlist('images')
    if data['image_name']!='none' and data.getlist('tags')!=[]:
        m_tags = data.getlist('tags')
        for image in images:
            img_obj =  Images.objects.create(title= data['image_name'],image=image)
            img_obj.save()
            img_obj.tags.add(*m_tags)
        messages.info(request,'upload successful !')
        return redirect('/')
    else:
        messages.info(request,'upload was not successful !')
        return redirect('/')

@api_view(['POST'])
def addtag(request):
    tagsserializers = TagsSerializers(data = request.data)
    if tagsserializers.is_valid():
        tagsserializers.save()
        return Response(tagsserializers.data)
    return tagsserializers(tagsserializers.errors)

@api_view(['GET'])
def get_all_tags(request):
    tags= Tag.objects.all()
    context = {
        'tags':tags,
    } 
    data = {'rendered_table': render_to_string('all-tags.html',context=context)}
    return JsonResponse(data)

@api_view(['GET'])
def laod_iamge_form(request):
    form = ImageFileUploadForm()
    context = {
        'form':form,
    } 
    data = {'rendered_table': render_to_string('forms.html',context=context)}
    return JsonResponse(data)


@api_view(['GET'])
def filter_data(request):
    tags = request.GET.getlist('tag[]')
    tags_obj = Tag.objects.all().distinct()
    print(tags)
    if tags!=[]:
        images = Images.objects.filter(tags__name__in=tags).distinct()
    else:
        images = Images.objects.all()
    print(images)
    context = {
        'images':images,
        'tags_obj':tags_obj,
        'tags':tags,
    }
    data = {'rendered_table': render_to_string('filter-images.html',context=context)}
    return JsonResponse(data)



@api_view(['GET','POST'])
def all_filter_tags(request):
    tags= Tag.objects.all().distinct()
    context = {
        'tags':tags,
    }
    #print(request.POST.getlist('check'))
    data = {'rendered_table': render_to_string('filter-tags.html',context=context)}
    return JsonResponse(data)


#request the id for the current item and read the file image and rotate the image and save it again
@api_view(['GET'])
def rotateimage(request,model_id=None,item_id=None,direction_val=None):
    #this code is for if you are saving images file in  media folder of localhost
    '''myModel = Images.objects.get(id=item_id)
    im = PilImage.open(myModel.image)
    rotated_image = im.rotate(direction_val)
    rotated_image.save(myModel.image.file.name, overwrite=True)'''

    #this code is when you are saving images in cloud i.e cloudnary
    image = Images.objects.get(id=item_id)
    image.direction = direction_val
    path = str(image.image.url).split('upload')
    image.url = f"{path[0]}upload/a_{image.direction}{path[1]}" 
    image.save()
    context = {
        'image':image,
    }
    data = render_to_string('test.html',context=context)
    return HttpResponse(data)

@api_view(['GET'])
def load_images(request,tags=None):
    if tags!= 'undefined':
        images = Images.objects.filter(tags__name__in=ast.literal_eval(tags))
    else:
        images = Images.objects.all()
    data = {}
    for image in images:
        data[image.id] = { 
        'id':image.id,
        'title':image.title,
        'image':image.image.url,
        'direction':image.direction,
        'url':image.url,
        'slug':image.slug,
        'created_at':image.created_at,
        'tags': image.tags.all().values(),
        'image_url_as_list':image.image_url_as_list(),
        'image_image_url_as_list':image.image_image_url_as_list()
    }
    return Response(data.values())




   

    




