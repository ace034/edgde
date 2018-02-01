import cloudinary.uploader

from cloudinary.forms import CloudinaryJsFileField
from django.forms.models import ModelForm

from .models import Video

class VideoUploadForm(ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'description', 'tags', 'channel', 'video')

class VideoDirectUploadForm(VideoUploadForm):
    video = CloudinaryJsFileField(
        attrs={'id':'channel_video'},
        options={
            'resource_type': 'video',
            'eager' : [{'streaming_profile' : "full_hd", 'format': "m3u8"}],
            'eager_async': 'true',
            'eager_notification_url' : 'http://localhost:8000/video/upload',
        }
    )
