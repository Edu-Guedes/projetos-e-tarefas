from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto
from .forms import ProjetoForm
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