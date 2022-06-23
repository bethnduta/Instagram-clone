from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import postListView
from .views import postCreateView

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', postCreateView.as_view(), name='post_create'),
    path('register/', views.register, name='register'),
    path('account/', include('django.contrib.auth.urls')),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
