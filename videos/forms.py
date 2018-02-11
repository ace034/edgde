import cloudinary.uploader

from django.forms.models import ModelForm

from .models import Video

class VideoUploadForm(ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'description', 'tags', 'channel', 'video')
