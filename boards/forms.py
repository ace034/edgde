from django.forms import ModelForm
from .models import *

class BoardCreationForm(ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'description', 'rating', 'image')
