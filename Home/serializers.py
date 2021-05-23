from rest_framework import serializers
from .models import Images
from taggit.models import Tag

class ImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['title','image','tags']


class TagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

