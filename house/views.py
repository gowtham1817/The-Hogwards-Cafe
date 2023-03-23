from django.shortcuts import render
from .models import Category

# Create your views here.
def home(request):
     return render(request, 'house/index.html')

def collections(request):
     category = Category.objects.filter(status=0)
     context = {'category':category}
     return render(request, 'house/collections.html',context)