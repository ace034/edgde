from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from cloudinary.forms import cl_init_js_callbacks

from .forms import VideoUploadForm, VideoDirectUploadForm

@method_decorator(login_required, name='dispatch')
class UploadView(View):
    template_name = 'videos/upload.html'
    form_class = VideoUploadForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        cl_init_js_callbacks(form, request)
        return render(request, self.template_name, {'form': form, 'direct': VideoDirectUploadForm})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return render(request, self.template_name, {'form': form, 'direct': VideoDirectUploadForm})

@method_decorator(csrf_exempt, name='dispatch')
class VideoDirectUploadComplete(View):
    def post(self, request, *args, **kwargs):
        form = VideoDirectUploadForm(request.POST)
        if form.is_valid():
            # Create a model instance for uploaded image using the provided data
            form.save()
            ret = dict(video_id = form.instance.id)
        else:
            ret = dict(errors = form.errors)

        return HttpResponse(json.dumps(ret), content_type='application/json')
