from django.urls import path
from . import views

urlpatterns = [
    path('auth/registro/', views.criar_usuario, name='criar_usuario'),
    path('auth/login/', views.logar_usuario, name='logar_usuario'),
]

