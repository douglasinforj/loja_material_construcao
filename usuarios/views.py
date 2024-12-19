from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

from rolepermissions.decorators import has_permission_decorator     #importamos as permissoes criadas no arquivo role


@has_permission_decorator('cadastra_vendedor')      #informamos qual a permissão o usuário que tiver poderá acessar
def cadastrar_vendedor(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastrar_vendedor.html')
    if request.method == "POST":
        #capturar dados do formulário:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        #verificar se email ja existe:
        user = Users.objects.filter(email=email)
        if user.exists():
            # TODO: Utilizar messages do DJango
            return HttpResponse('Email já existe')
        
        #caso não exista:
        user = Users.objects.create_user(username=email, email=email, password=senha, cargo="V") #o django utiliza o username para autenticar, vamos injetar o email no user name

        # TODO: Redirecionar com uma mensagem
        return HttpResponse('Conta criada')