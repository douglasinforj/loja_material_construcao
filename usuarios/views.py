from django.shortcuts import render
from django.http import HttpResponse

from rolepermissions.decorators import has_permission_decorator     #importamos as permissoes criadas no arquivo role


@has_permission_decorator('cadastra_vendedor')      #informamos qual a permissão o usuário que tiver poderá acessar
def cadastrar_vendedor(request):
    return render(request, 'usuarios/cadastrar_vendedor.html')
