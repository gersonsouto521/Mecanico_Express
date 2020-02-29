from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm

def home(request):
    return render(request,'index.html')

def contato_teste(request):
    return render(request,'contato2.html')

def contato(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Formulário de Contatos",
        "content": "Bem-vindo a pagina de contato",
        "form": contact_form,
    }
    if request.method == "POST":
        print(request.POST)
    return render(request,'contato.html',context)




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