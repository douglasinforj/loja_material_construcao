from django.db import models

class Categoria(models.Model):
    titulo = models.CharField(max_length=40)

    def __str__(self):
        return self.titulo
    
class Produto(models.Model):
    nome = models.CharField(max_length=40)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    quantidade = models.FloatField()
    preco_compra = models.FloatField()
    preco_venda = models.FloatField()        #models.BinaryField()     #melhor foamto para calculos de valores, evita problemas com calculos flutuantes

    def __str__(self):
        return self.nome

    #metodo gerar desconto
    def gerar_desconto(self, desconto):
        return  self.preco_venda -  ((self.preco_venda * desconto) / 100)
    
    #metodo calcular o lucro
    def lucro(self):
        lucro = self.preco_venda - self.preco_compra
        return (lucro * 100) / self.preco_compra
    

class Imagem(models.Model):
    imagem = models.ImageField(upload_to="image_produto")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)