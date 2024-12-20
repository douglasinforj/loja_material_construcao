from django.shortcuts import render
from .models import Categoria, Produto, Imagem

from  django.http import HttpResponse

#tratando as imagens
from datetime import date
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


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
            #tratando a image antes de salvar:
            name = f'{date.today()} - {produto.id}.jpg'        # biblioteca (((from datetime import date))

            img = Image.open(f)                            #opencv abre a imagem vindo a iteração 'f'    ((from PIL import Image))
            img = img.convert('RGB')                       #garantir conversão para RGB
            img = img.resize((300, 300))                   #dimensionando a imagem
            draw = ImageDraw.Draw(img)                        #marca d'agua ((from PIL import imageDraw)) escreve em imagem do pillow
            draw.text((20, 280), f"Loja Construct {date.today()}", (255,255,255))    #texto que será adicionado no canto inferior esquerdo
            output = BytesIO()                                     #Instanciando BytesIO em output, aceita bytes ((from io import BytesIO))
            img.save(output, format="JPEG", quality=100)           #convertendo para que o django entenda 
            output.seek(0)                                         #colocando ponteiro para o inicio da instrução
            #Convertendo o output para InMemoryUploadedFile  ((from django.core.files.uploadedfile import InMemoryUploadedFile))
            img_final = InMemoryUploadedFile(output,
                                             'ImageField', 
                                             name,
                                             'IMAGE/jpg',
                                              sys.getsizeof(output),   # para buscar o tamanho da imagem ((import sys)), passamos os bytes
                                              None                    #nada com texto
                                              )

            img_dJ = Imagem(imagem = img_final, produto=produto)      #ai podemos passa o "img_final" após o tratamento da imagem
            img_dJ.save()
        return HttpResponse('Foi enviada!')


