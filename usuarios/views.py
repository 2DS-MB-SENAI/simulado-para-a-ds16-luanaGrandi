from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def criar_usuario(request):
    nome = request.data.get('nome')
    senha = request.data.get('senha')
    telefone = request.data.get('telefone')
    if not telefone :
        return Response({'Erro': 'Campos obrigatorios imcompletos'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(nome=nome).exists():
         return Response({'Erro': f'username {nome} já existe'},  status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(telefone=telefone).exists():
        return Response({'Erro': f'O numero de telefone: {telefone} já existe'},  status=status.HTTP_400_BAD_REQUEST)
    
    usuario = User.objects.create_user(
        nome=nome,
        senha=senha,
        telefone = telefone,
    )
    return Response({'mensagem': f'Usuario {nome} criado com sucesso'},  status=status.HTTP_201_CREATED)


@api_view(['POST'])
def logar_usuario(request):
    nome = request.data.get('nome')
    senha = request.data.get('senha')
    usuario = authenticate(nome=nome, password = senha)

    if usuario:
       refresh =  RefreshToken.for_user(usuario)
       return Response({
           'acesso': str(refresh.access_token),
            'refresh' : str(refresh)
        }, status=status.HTTP_200_OK)
    
    else:
        return Response({'erro': 'Usuario ou/e senha incorreto(s)'}, status=status.HTTP_401_UNAUTHORIZED)