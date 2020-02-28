from django.shortcuts import render
from django.Http import HttpResponse


# Create your views here.
def index(request):
  images = Image.objects.all()
  return render(request, "landing/index.html", {"image":images})

def category(request, id):
    '''
    method to search images category
    '''
    images = Image.Object.filter(category_id=id)
    context = {
        "categories":categories
        "images":images
    }
    return render(request, 'landing/search_result.html',context)