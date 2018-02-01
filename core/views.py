from django.shortcuts import render
import cloudinary, cloudinary.uploader, cloudinary.forms
# Create your views here.
from django import forms
from django.http import HttpResponse

from cloudinary.forms import cl_init_js_callbacks
from .models import Photo
from .forms import PhotoDirectForm

class UploadFileForm(forms.Form):
    image  = cloudinary.forms.CloudinaryJsFileField()

def save(request):
    form = UploadFileForm(request.POST)
    cloudinary.forms.cl_init_js_callbacks(form, request)
    if request.method == 'POST':
        if form.is_valid():
            image = form.cleaned_data['image']
            return HttpResponseRedirect(image.url())
    return render_to_response('posts/upload.html',
                              RequestContext(request, {'form': form, 'post': p}))
def upload_prompt(request):
  context = dict(direct_form = PhotoDirectForm())
  cl_init_js_callbacks(context['direct_form'], request)
  return render(request, 'upload_prompt.html', context)

  @csrf_exempt
def direct_upload_complete(request):
  form = PhotoDirectForm(request.POST)
  if form.is_valid():
    form.save()
    ret = dict(photo_id = form.instance.id)
  else:
    ret = dict(errors = form.errors)

  return HttpResponse(json.dumps(ret), content_type='application/json')
