from django.urls import path
from . import views

urlpatterns = [
    path('clip_list/', views.clip_list, name='clip_list'),
]
