from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.logar, name="login"),
    path('', views.home, name="home"),
    path('sair/', views.sair, name="sair"),
]