from django.urls import path, include
from .forms import *
from .views import BoardCreateView, BoardCreationForm, BoardDetailView, BoardAddCommentView

app_name = 'boards'
urlpatterns = [
    path('', BoardCreateView.as_view(), name='index'),
    path('<str:pk>', BoardDetailView.as_view(), name='detail'),
    path('<str:pk>/comment', BoardAddCommentView.as_view(), name='add-comment'),
]
