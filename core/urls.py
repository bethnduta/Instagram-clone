from django.urls import path,include
from .views import postListView

urlpatterns = [
    path('', postListView.as_view(), name='index'),
]