from django.shortcuts import render
from .models import Categoria, Produto, Imagem

from  django.http import HttpResponse

def add_produto(request):
    #tipos de requisição
    if request.method == "GET":
        categorias = Categoria.objects.all()
        return render(request, 'estoque/add_produto.html', {'categorias': categorias })
    
    elif request.method == "POST":
        #capturando dos dados da template
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        quantidade = request.POST.get('quantidade')
        preco_compra = request.POST.get('preco_compra')
        preco_venda = request.POST.get('preco_venda')
        imagens = request.FILES.getlist('imagens')
        
        #salvar no banco
        produto = Produto(nome=nome, categoria_id=categoria, quantidade=quantidade, preco_compra=preco_compra, preco_venda=preco_venda)
        produto.save()

        #salvando as imagens
        for f in request.FILES.getlist('imagens'):   #como são varias imagens, vamos iterar usando for.
            img = Imagem(imagem = f, produto=produto)
            img.save()
        return HttpResponse('Foi enviada!')


