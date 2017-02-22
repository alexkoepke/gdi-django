from django.shortcuts import render


def gallery(request):

    context = {

    }

    return render(request, 'gallery/gallery.html', context)
