from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    products = Articles.objects.all()
    jewelleries = Articles.objects.filter(type = 'jewellery')
    potraits = Articles.objects.filter(type = "potrait")
    crochets = Articles.objects.filter(type = 'crochet')
    return render(request, 'index.html', {'products' : products, 'jewelleries' : jewelleries, 'potraits' : potraits, 'crochets' : crochets})


def redirect_to_store(request):
    return redirect("https://thedesigndiary.mini.site")

def redirect_to_insta(request):
    return redirect("https://www.instagram.com/_the.designdiary_?igsh=MWI1NGQzcWpjdXZ3cw==")