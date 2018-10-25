from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'miniobservium/index.html',{})

# Create your views here.
