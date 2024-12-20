from django.shortcuts import render

def add_produto(request):
    return render(request, 'estoque/add_produto.html')
