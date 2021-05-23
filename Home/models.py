from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from taggit.managers import TaggableManager


# Create your models here.
class Images(models.Model):
    title = models.CharField(max_length=225,blank=True,null=True)
    image = CloudinaryField(
        "image",
        overwrite=True,
        resource_type="image",
        transformation={"quality": "auto:eco"},
        format="jpg",
    )
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


'''class Tags(models.Model):
    word = models.CharField(max_length=100)
    slug = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def _get_unique_slug(self):
        slug = slugify(self.word)
        unique_slug = slug
        num = 1
        while Tags.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.word'''
    
