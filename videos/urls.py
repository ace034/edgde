from django.urls import path, include

from .views import UploadView, VideoView

app_name = 'videos'
urlpatterns = [
    path('upload', UploadView.as_view(), name='upload'),
    path('<str:pk>', VideoView.as_view(), name='view'),
]
