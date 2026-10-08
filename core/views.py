from django.shortcuts import render, redirect
from .models import Projeto
from .forms import ProjetoForm

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