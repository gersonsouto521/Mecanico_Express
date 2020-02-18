from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def embreagem(request):
    return render(request,'services/embreagem.html')