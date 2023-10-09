from django.urls import path
from pagina import views

urlpatterns = [
    path('', views.home, name='url_pagina'),
    path('contato/', views.contato, name='contato'),
    path('inserir_contato', views.inserir_contato, name='inserir_contato'),
    path('sucesso/', views.pagina_sucesso, name='sucesso'),
    path('mensagens/', views.mensagens, name='mensagens'),
    # passando id como parâmetro para editar contato específico
    path('editar_contato/<int:contato_id>/', views.editar_contato, name='editar_contato'),
    path('delete/<int:contato_id>/', views.tela_deletar_contato, name='tela_deletar'),
    path('deletando/<int:contato_id>/', views.deletar_contato, name='deletar')
]
