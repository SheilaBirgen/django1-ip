from django.shortcuts import render
from django.Http import HttpResponse


# Create your views here.
def index(request):
  return render(request, "landing/index.html")