from django import forms
from .models import Projeto
from django import forms
from .models import Projeto, Tarefa

class ProjetoForm(forms.ModelForm):

    class Meta:
        model = Projeto

        fields = ['nome', 'descricao', 'data_inicio']

        widgets = { 'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome do projeto'
                }),

            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descrição do projeto',
                    'rows': 5
                }),

            'data_inicio': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }),
        }


class TarefaForm(forms.ModelForm):

    class Meta:
        model = Tarefa

        fields = [
            'titulo',
            'prioridade',
            'concluido',
            'projeto'
        ]

        labels = {
            'titulo': 'Título da tarefa',
            'prioridade': 'Prioridade',
            'concluido': 'Tarefa concluída',
            'projeto': 'Projeto',
        }

        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Título da tarefa',
                    'maxlength': 200
                }
            ),

            'prioridade': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'concluido': forms.CheckboxInput(
                attrs={
                    'class': 'form-checkbox'
                }
            ),

            'projeto': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }