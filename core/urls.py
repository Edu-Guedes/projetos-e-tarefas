from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path("projetos/", views.projeto_lista, name="projeto_lista"),
    path("projetos/novo/", views.projeto_criar, name="projeto_criar"),
    path("projetos/<int:pk>/editar/", views.projeto_editar, name="projeto_editar"),
    path("projetos/<int:pk>/excluir/", views.projeto_excluir, name="projeto_excluir"),
]