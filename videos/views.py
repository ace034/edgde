from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Video
from .forms import VideoUploadForm

@method_decorator(login_required, name='dispatch')
class UploadView(View):
    template_name = 'videos/upload.html'
    form_class = VideoUploadForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'direct': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            model = form.save()
            return redirect('videos:view', pk=model.pk)

        return render(request, self.template_name, {'form': form, 'direct': self.form_class})


@method_decorator(login_required, name='dispatch')
class VideoView(View):
    template_name = 'videos/view.html'
    
    def get(self, request, *args, **kwargs):
        # Get our model and increase by a view.
        model = get_object_or_404(Video, pk=self.kwargs['pk'])

        # Take a fee.
        if request.user != model.channel.owner:
            model.views += 1
            model.save()
            request.user.points -= model.view_fee
            request.user.save()

        # Get the file type.
        file_type = model.video.url.split('.')[-1]

        return render(request, self.template_name, {
            'model': model,
            'file_type': file_type
        })