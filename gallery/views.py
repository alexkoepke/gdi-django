from django.shortcuts import render

# Create your views here.
def gallery(request):



    context = {
        'gallery_list': ['vacation', 'cat photos', 'more cat photos', 'stuff']
    }

    return render(request, 'gallery/gallery.html', context)
