from django.urls import path
from pagina import views

urlpatterns = [
    path('', views.home, name='url_pagina'),
    path('contato/', views.contato, name='contato'),
]
