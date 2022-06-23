from core.forms import postForm
from .models import *
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm



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
    queryset=Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    

class postCreateView(CreateView):
    template_name = 'insta/post_create.html'
    form_class = postForm
    queryset=Post.objects.all()
    succes_url='/'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.save(commit=False)
        form.instance.author = self.request.user
        form.save()
        return redirect('index')

@login_required(login_url='login')
def index(request):
    return render(request, 'registration/login.html')    


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            form.save()
        return redirect('login')
        
    else:    
        form = UserRegisterForm()
    return render(request,'registration/register.html',{'form':form})


def unfollow(request, to_unfollow):
    if request.method == 'GET':
        user_profile2 = Profile.objects.get(pk=to_unfollow)
        unfollow_d = Follow.objects.filter(follower=request.user.profile, followed=user_profile2)
        unfollow_d.delete()
        return redirect('userprofile', user_profile2.user.username)


def follow(request, to_follow):
    if request.method == 'GET':
        user_profile3 = Profile.objects.get(pk=to_follow)
        follow_s = Follow(follower=request.user.profile, followed=user_profile3)
        follow_s.save()
        return redirect('userprofile', user_profile3.user.username)  

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Account updated successfully')
            return redirect('profile')
    u_form=UserUpdateForm(instance=request.user)
    p_form=ProfileUpdateForm(instance=request.user)

    context={'u_form':u_form,'p_form':p_form}
    return render(request,'insta/profile.html',context)


       