from cProfile import label
from dataclasses import fields
from pyexpat import model
from ..models import Produto
from django.forms import ModelForm
from django import forms

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'custo', 'preco', 'fornecedor', 'quantidade', 'peso','tipo',"temVarejo"]