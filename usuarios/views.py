from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

from rolepermissions.decorators import has_permission_decorator     #importamos as permissoes criadas no arquivo role

from django.shortcuts import redirect     #faz o redirecionamento de pagina
from django.urls import reverse           #transforma o nome da url na url de fato   
from django.contrib import auth           #modulo verifica autenticação




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

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:           #caso  o usuario esteja logado
            return redirect(reverse('plataforma'))       #reverse esta transformando o nome na urls completa
        return render(request, 'usuarios/login.html')        #caso não esteja logado é retornado a pagina de login
    #caso não loogado
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        #verifica se os dados são validos do banco de dados:
        user = auth.authenticate(username=login, password=senha)

        if not user:
            #TODO: Redirecionar com mensagem de erro
            return HttpResponse('Usuário inválido')
        
        #se ele existe:
        auth.login(request, user)
        #TODO: tratar do redirecionamento
        return HttpResponse('Usuário logado com sucesso')
