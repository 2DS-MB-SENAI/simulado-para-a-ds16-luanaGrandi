from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import LivroSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Livro

def listar_livro(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})


@api_view(['GET', 'POST'])
def read_livros(request):
    if request.method == 'GET' :
        livros = Livro.objects.all()
        serializer = LivroSerializer (livros, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = LivroSerializer(data = request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


