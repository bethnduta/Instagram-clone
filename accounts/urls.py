from django.urls import URLPattern, path,include
from . import views


urlpatterns=[
    path('',views.index,name='account'),
     path('register/', views.register, name='register'),
]