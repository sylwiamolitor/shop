from django.shortcuts import render
from .models import Carousel

def index(request):
    carousel = Carousel.objects.all()
    context  = {
        'carousel' : carousel
    }
    return render(request, 'index.html', context)