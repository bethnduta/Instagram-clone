from django.urls import path,include
from .views import postListView
from .views import postCreateView

urlpatterns = [
    path('', postListView.as_view(), name='index'),
    path('new/', postCreateView.as_view(), name='post_create'),
]