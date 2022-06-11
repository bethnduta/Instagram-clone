from core.forms import postForm
from .models import post
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
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
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            messages.success(request, f'Your account has been created. You can log in now!')   
          
            return redirect('index')
    else:
        form = UserRegistrationForm()

    
    return render(request, 'registration/register.html', {'form':form})       