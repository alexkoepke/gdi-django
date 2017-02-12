from django.shortcuts import render

# Create your views here.
def gallery(request):

    gallery_list = ["vacation", "cat photos", "more cat photos"]

    context = {
        'gallery_list': gallery_list
    }

    return render(request, 'gallery/gallery.html', context)
