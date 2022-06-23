from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import postListView
from .views import postCreateView

urlpatterns = [
    
    path('', views.postListView.as_view(),name='home'),
    path('new/', postCreateView.as_view(), name='post_create'),
    path('register/', views.register, name='register'),
    path('profile/<username>/', views.profile, name='profile'),
    path('account/', include('django.contrib.auth.urls')),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow'),
    path('userprofile/<username>/', views.userprofile, name='userprofile'),
    path('like_post/<id>/',views.like_post, name='like_post'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
