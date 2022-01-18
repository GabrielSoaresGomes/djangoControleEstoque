from pyexpat import model
from django.db import models


class Produto(models.Model):
    descricao = models.CharField("Descrição", max_length=200, null=True)
    custo = models.DecimalField("Custo", max_digits=7, decimal_places=2, null=True)
    preco = models.DecimalField("Preço", max_digits=7, decimal_places=2, null=True)
    fornecedor = models.CharField("Fornecedor", max_length=100, null=True)
    quantidade = models.SmallIntegerField("Quantidade", null=True)
    peso = models.SmallIntegerField("Peso", null=True)

class Fornecedor(models.Model):
    nome = models.CharField("Nome", max_length=100)
    cnpj = models.CharField("CNPJ", max_length=22)