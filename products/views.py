from django.shortcuts import render
from .models import Cakes
from .models import Homepage

def home(request):
    imagehome=Homepage.objects.all()
    return render(request,'products/home.html',{'imagehome':imagehome})


def products(request):
    cakes=Cakes.objects.all()
    return render (request,'products/product.html',{'cakes':cakes})
