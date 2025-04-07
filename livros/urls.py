from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.listar_livro, name='listar_livros'),
    path('api/livros/', views.read_livros, name='read_livros'),
]