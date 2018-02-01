from django.urls import path, include

app_name = 'core'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profilepic', UploadFileForm.as_view(), name='profilepic')
]
