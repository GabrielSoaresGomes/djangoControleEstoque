from dataclasses import fields
from ..models import Produto
from django.forms import ModelForm

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'custo', 'preco', 'fornecedor', 'quantidade', 'peso']