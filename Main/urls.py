"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    path('api/addtag/',addtag,name='addtag'),
    path('api/addimage/',addimage,name='addimage'),
    path('ajax/load-tags/',get_all_tags, name='get_all_tags'),
    #path('ajax/load-image-form/',laod_iamge_form, name='laod_iamge_form'),
    path('filter-data',filter_data,name='filter_data'),
    path('ajax/all/filter/tags/',all_filter_tags,name="all_filter_tags"),
    path('rotateimage/<str:model_id>/<str:item_id>/<str:direction_val>/',rotateimage,name="rotateimage"),
    path('ajax/load-images/<str:tags>/',load_images,name="load_images")
    
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)