from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm
from django.contrib import messages
# Create your views here.



def projeto_lista(request):
    projetos = Projeto.objects.all()

    return render(
        request,
        'core/projeto_lista.html',
        {'projetos': projetos}
    )


def projeto_criar(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('core:projeto_lista')
    else:
        form = ProjetoForm()

    return render(
        request,
        'core/projeto_form.html',
        {'form': form}
    )


def projeto_editar(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('core:projeto_lista')

    else:
        form = ProjetoForm(instance=projeto)

    return render(
        request,
        'core/projeto_form.html',
        {
            'form': form,
            'projeto': projeto
        }
    )


def projeto_excluir(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto excluído com sucesso!')
        return redirect('core:projeto_lista')

    return render(
        request,
        'core/projeto_confirmar_exclusao.html',
        {'projeto': projeto}
    )


def tarefa_lista(request):
    tarefas = Tarefa.objects.select_related('projeto').all().order_by('concluido', 'prioridade', 'titulo')

    return render(request, 'core/tarefa_lista.html',{'tarefas': tarefas})

def tarefa_criar(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa cadastrada com sucesso!')
            return redirect('core:tarefa_lista')
    else:
        form = TarefaForm()
        return render(request, 'core/tarefa_form.html', {'form': form})


def tarefa_editar(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('core:tarefa_lista')
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'core/tarefa_form.html', {'form': form, 'tarefa': tarefa})

def tarefa_excluir(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('core:tarefa_lista')

    return render(request, 'core/tarefa_confirmar_exclusao.html', {'tarefa': tarefa})
   

