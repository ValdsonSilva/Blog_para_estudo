from django.shortcuts import render

# Create your views here.


def home(request):
    
    mensagem = { 
                'eu' : 'valdson' ,
                'namorada' : 'Joelyne meu amor!'
    }
    
    return render(request, 'home.html', mensagem)


def contato(request):
    
    mensagem = {'mensagem':"Formulário"}
    
    return render(request, 'contato.html', mensagem)