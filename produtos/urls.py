from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.produtosList, name="produtosList"),
    path('/addProdutos', views.adicionarProdutos,name="adicionarProdutos"),
    path('/editProdutos/<int:id>', views.atualizarProdutos, name="atualizarProdutos")
]