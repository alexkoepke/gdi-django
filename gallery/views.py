from django.shortcuts import render
from gallery.models import GalleryItem


def gallery(request):

    context = {
        'items': GalleryItem.objects.all(),
    }

    return render(request, 'gallery/gallery.html', context)
