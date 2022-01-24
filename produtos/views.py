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

def atualizarProdutos(request, id):
    produto = Produto.objects.get(id=id)
    produtoForm = ProdutoForm(request.POST or None, instance=produto)
    if produtoForm.is_valid():
        produtoForm.save()
        return redirect('produtosList')
    return render(request, "adicionarProduto.html", {"produtoForm": produtoForm, "produto": produto})
