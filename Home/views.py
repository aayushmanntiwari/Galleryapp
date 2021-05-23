import io
from io import StringIO
from PIL import Image
from django.http.response import HttpResponse, JsonResponse
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
    if tags!=[]:
        images = Images.objects.filter(tags__name__in=tags).distinct()
    else:
        images = Images.objects.all()
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
def rotateimage(request,id): 
    myModel = Images.objects.get(pk=id)
    original_photo = StringIO.StringIO(myModel.file.read())
    rotated_photo = StringIO.StringIO()
    image = Image.open(original_photo)
    image = image.rotate(-90) or image.rotate(90) #we get this value through post form 
    image.save(rotated_photo, 'JPEG')

    myModel.file.save(image.file.path, ContentFile(rotated_photo.getvalue()))
    myModel.save()

    return render(request, '...',{...})
    




