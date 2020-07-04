from django.shortcuts import render, redirect
from .models import Processo

# Create your views here.

def lista(request):
    lista = Processo.objects.all()

    return render(request, 'principal/processos.html', {'lista': lista})
