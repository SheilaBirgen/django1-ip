from django.shortcuts import render
from .models import Image,Categories,Location
from django.views.generic import TemplateView, ListView


# Create your views here.
def index(request):

  images = Image.objects.all()

  return render(request,'index.html',{'images':images})

def search_results(request):
    '''
    Method to search location or category
    '''
    if 'image' in request.GET and request.GET["image"]:
        search_category = request.GET['image']
        searched_images = Image.search_images(search_category)
        message = f'{search_category}'

        context = {
            'message': message,
            'images': searched_images,
        }
        return render(request, 'search_result.html', context)
    else:
        message ='The category does not exist!!'
        contect={
            'message':message,
        }
        return render(request, 'landing/search_results.html', {"message":message})
      
def category(request, id):
    '''
    method to search images category
    '''
    images = Image.Object.filter(category_id=id)
    context = {
        "categories":categories,
        "images":images
    }

    return render(request, 'landing/search_result.html', context)