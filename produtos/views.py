from django.shortcuts import render,redirect
from .models import Produto
from .forms.produtoForm import ProdutoForm

def produtosList(request):
    produtos = Produto.objects.all()
    return render(request, 'listaProdutos.html', {'produtos': produtos})

def adicionarProdutos(request):
    produtoForm = ProdutoForm
    if produtoForm.is_valid:
        produtoForm.save()
        return redirect('produtosList')
    return render(request, "estadioForm.html", {"produtoForm": produtoForm})
