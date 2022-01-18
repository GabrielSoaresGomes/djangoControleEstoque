from django.urls import path, include
from .views import produtosList, adicionarProdutos

urlpatterns = [
    path("",produtosList, name="produtosList"),
    path('addProdutos/', adicionarProdutos,name="adicionarProdutos"),
]