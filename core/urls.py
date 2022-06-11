from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import postListView
from .views import postCreateView

urlpatterns = [
    path('home/', postListView.as_view(), name='index'),
    path('new/', postCreateView.as_view(), name='post_create'),
    path('',views.index,name='account'),
    path('register/', views.register, name='register'),
    path('account/', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
