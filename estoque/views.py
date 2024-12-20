from django.shortcuts import render
from .models import Categoria

def add_produto(request):
    #tipos de requisição
    if request.method == "GET":
        categorias = Categoria.objects.all()
        return render(request, 'estoque/add_produto.html', {'categorias': categorias })
