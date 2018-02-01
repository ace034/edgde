from django.urls import path, include

from .views import UploadView, VideoDirectUploadComplete

app_name = 'video'
urlpatterns = [
    path('upload', UploadView.as_view(), name='upload'),
    path('upload/complete', VideoDirectUploadComplete.as_view(), name='complete'),
]
