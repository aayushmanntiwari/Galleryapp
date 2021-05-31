from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from taggit.managers import TaggableManager


# Create your models here.
class Settings(models.Model):
    cloud_name = models.CharField(max_length=225,blank=True,null=True)
    api_key = models.CharField(max_length=225,blank=True,null=True)
    api_secret = models.CharField(max_length=225,blank=True,null=True)

class Images(models.Model):
    title = models.CharField(max_length=225,blank=True,null=True)
    image = CloudinaryField(
        "image",
        overwrite=True,
        resource_type="image",
        transformation={"quality": "auto:eco"},
        format="jpg",
    )
    direction = models.IntegerField(default=0,blank=True,null=True)
    url = models.CharField(max_length=225,blank=True,null=True)
    slug = models.SlugField(blank=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Images.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def image_url_as_list(self):
        if self.url is not None:
            path = self.url.split('upload')
            return f"{path[0]}upload/fl_attachment:{self.title}{path[1]}"
        else:
            return '' 
    
    def image_image_url_as_list(self):
        if self.image is not None:
            if 'upload' in self.image.url:
                path = self.image.url.split('upload')
                return f"{path[0]}upload/fl_attachment:{self.title}{path[1]}"
            else:
                return ''
        else:
            return '' 



    
