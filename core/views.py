from core.forms import postForm
from .models import post
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import UserRegisterForm
from django.views.generic import (
    ListView,
    CreateView,
    )

# Create your views here.
class postListView(ListView):
    template_name = 'insta/index.html'
    context_object_name = 'posts'
    queryset=post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    


class postCreateView(CreateView):
    template_name = 'insta/post_create.html'
    form_class = postForm
    queryset=post.objects.all()
    succes_url='/'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)

def index(request):
    return render(request, 'registration/login.html')    


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            form.save()
        return redirect('post_create')
        
    else:    
        form = UserRegisterForm()
    return render(request,'registration/register.html',{'form':form})