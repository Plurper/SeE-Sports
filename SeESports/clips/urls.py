from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('clip_list/', views.clip_list, name='clip_list'),
    path('videos/', views.videos, name='videos'),
]
