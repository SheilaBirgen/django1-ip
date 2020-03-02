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
    if 'result' in request.GET and request.GET["result"]:
        search_term = request.GET.get("result")
        searched_images = Image.search_by_category(search_term)
       
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "images":searched_images})
    else:
        message = "You haven't searched for any term"
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