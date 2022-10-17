import json
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Cadastro
from .models import FormCadastro
from convert import xlsx, csv
from random import choice
import string


def index(request):
    cadastros = Cadastro.objects.get_queryset().order_by('id')
    paginator = Paginator(cadastros, 10)
    page = request.GET.get('p')
    cadastros = paginator.get_page(page)
    pegar()
    return render(request, 'cadastro/index.html', {
        'cadastros': cadastros
    })


def pegar():
    cadastros = Cadastro.objects.all()
    lista = []
    for cadastro in cadastros:
        lista.append(({'login': cadastro.login,
                       'senha': cadastro.senha,
                       'data_de_nascimento': cadastro.data_de_nascimento}))
    with open("C:/Users/Ivson/PycharmProjects/Frexco/templates/static/users.json", "w") as jf:
        json.dump(lista, jf, indent=4, default=str)
    csv()
    xlsx()


def ver_usuario(request, cadastro_id):
    cadastro = Cadastro.objects.get(id=cadastro_id)
    return render(request, 'cadastro/ver_usuario.html', {
        'cadastro': cadastro
    })


def cadastrar_user(request):
    if request.method != 'POST':
        form = FormCadastro(initial={'senha': senha_alea()})
        return render(request, 'cadastro/cadastro_user.html', {'form': form})
    form = FormCadastro(request.POST, request.FILES)

    if not form.is_valid():
        form = FormCadastro(request.POST)
        return render(request, 'cadastro/cadastro_user.html', {'form': form})

    form.save()
    return redirect('cadastrar_user')

def senha_alea():
    tamanho = 10
    valores = string.ascii_lowercase + string.digits
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)
    print(senha)
    return senha
