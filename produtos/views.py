from django.shortcuts import render,redirect
from .models import Produto
from .forms.produtoForm import ProdutoForm

def produtosList(request):
    produtos = Produto.objects.all()
    return render(request, 'listaProdutos.html', {'produtos': produtos})

def adicionarProdutos(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produtosList')
    return render(request, "adicionarProduto.html", {"produtoForm": form})
