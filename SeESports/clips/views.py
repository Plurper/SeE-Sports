from django.shortcuts import render
from .models import Clip

def clip_list(request):
    clips = Clip.objects.all()
    return render(request, 'clip_list.html', {'clips': clips})