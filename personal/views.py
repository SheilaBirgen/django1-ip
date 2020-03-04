from django.shortcuts import render
from .models import Image,Categories,Location
from django.views.generic import TemplateView, ListView

# Create your views here.
def index(request):

  images = Image.objects.all()

  return render(request,'index.html',{'images':images})

def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'landing/search.html',{"message":message,"articles": searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'landing/search.html',{"message":message})
        
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

