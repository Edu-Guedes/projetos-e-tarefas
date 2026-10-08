from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path("projetos/", views.projeto_lista, name="projeto_lista"),
    path("projetos/novo/", views.projeto_criar, name="projeto_criar"),
    path("projetos/<int:pk>/editar/", views.projeto_editar, name="projeto_editar"),
    path("projetos/<int:pk>/excluir/", views.projeto_excluir, name="projeto_excluir"),
    path("tarefas/", views.tarefa_lista, name="tarefa_lista"),
    path("tarefas/nova/", views.tarefa_criar, name="tarefa_criar"),
    path("tarefas/<int:pk>/editar/", views.tarefa_editar, name="tarefa_editar"),
    path("tarefas/<int:pk>/excluir/", views.tarefa_excluir, name="tarefa_excluir"),
]