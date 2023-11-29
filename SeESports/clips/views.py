from django.shortcuts import render
from .models import Clip
from .models import Video

def clip_list(request):
    clips = Clip.objects.all()
    return render(request, 'clip_list.html', {'clips': clips})

def home_page(request):
    return render (request, 'clips/home_page.html')

def videos(request):
    video=Video.objects.all()
    return render (request, 'videos.html')

def aboutme(request):
    return render (request, 'aboutme.html')