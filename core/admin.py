from django.contrib import admin
from .models import Projeto, Tarefa

# Register your models here.

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio')
    search_fields = ('nome',)

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'prioridade', 'concluido', 'projeto')
    list_filter = ('prioridade', 'concluido', 'projeto')
    search_fields = ('titulo',)