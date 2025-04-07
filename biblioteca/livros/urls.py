from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_livro, name='listar_livros'),
]