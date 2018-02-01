from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
# Create your views here.
from .models import *
from .forms import BoardCreationForm

class BoardCreateView(View):
    template_name = 'boards/create.html'
    form_class = BoardCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.owner = request.user
            model.save()

            model.members.add(request.user)
            # TODO: NO NEVER THIS AGAIN.
            # user = authenticate(
            #     request,
            #     username=form.cleaned_data['username'],
            #     password=form.cleaned_data['password1']
            # )
            # login(request, user)

            return redirect('boards:index')

        return render(request, self.template_name, {'form': form})

class BoardDetailView(View):
    template_name = 'boards/detail.html'

    def get(self, request, *args, **kwargs):
        model = get_object_or_404(Board, pk=self.kwargs['pk'])
        return render(request, self.template_name,{'model':model})
