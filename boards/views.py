from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from .forms import BoardCreationForm, PostCreationForm
from .models import *


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

            return redirect('boards:index')

        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class BoardDetailView(View):
    template_name = 'boards/detail.html'

    def get(self, request, *args, **kwargs):
        model = get_object_or_404(Board, pk=self.kwargs['pk'])
        return render(request, self.template_name,{'model':model, 'form': PostCreationForm})

@method_decorator(login_required, name='dispatch')
class BoardAddCommentView(View):
    form_class = PostCreationForm
    def post(self, request, *arg, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            model = form.save(commit=False)
            model.account = request.user
            model.board = get_object_or_404(Board, pk=self.kwargs['pk'])
            model.save()

        return redirect('boards:detail', pk=model.board.pk)
