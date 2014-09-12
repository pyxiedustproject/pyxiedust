from django.shortcuts import render

from .models import Photo


def gallery(request):
    photos = Photo.objects.all()
    return render(request, 
        'photos/gallery.html',
        {'photos': photos},
    )
