from django.shortcuts import render
from .models import Livro

def listar_livro(request):
    listar = Livro.objects.all()
    return render(request, 'biblioteca/listar_livros.html', {'listar': listar})
