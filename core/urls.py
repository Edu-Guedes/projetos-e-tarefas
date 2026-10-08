from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path("projetos/", views.projeto_lista, name="projeto_lista"),
    path("projetos/novo/", views.projeto_criar, name="projeto_criar"),
]