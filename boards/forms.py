from django.forms import ModelForm
from .models import *

class BoardCreationForm(ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'description', 'rating', 'image')

class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')