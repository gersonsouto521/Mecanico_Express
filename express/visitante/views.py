from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def contato(request):
    return render(request,'contato.html')

def sobre(request):
    return render(request,'sobre.html')

def servicos(request):
    return render(request,'servicos.html')

def embreagem(request):
    return render(request,'services/embreagem.html')

def suspensao(request):
    return render(request,'services/suspencao.html')

def escapamento(request):
    return render(request,'services/escapamento.html')

def injecao(request):
    return render(request,'services/injecao.html')

def freios(request):
    return render(request,'services/freios.html') 

def manutencao_preventiva(request):
    return render(request,'services/manutencao_preventiva.html')  