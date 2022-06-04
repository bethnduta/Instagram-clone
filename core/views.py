from .models import post
from django.shortcuts import render
from django.views.generic import (
    ListView
    )

# Create your views here.
class postListView(ListView):
    template_name = 'insta/index.html'
    context_object_name = 'posts'
    queryset=post.objects.all()