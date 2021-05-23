from django import forms
from .models import Images


class ImageFileUploadForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('title', 'image')