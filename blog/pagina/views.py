from django.shortcuts import render, redirect, HttpResponse
from .models import Contato
from .form import ContatoForm # formulário

# Create your views here.


def home(request):
    
    mensagem = { 
                'eu' : 'valdson' ,
                'namorada' : 'Joelyne meu amor!'
    }
    
    return render(request, 'home.html')


# tela de listagem das mensagens
def mensagens(request):
    
    # pegando todos os contatos registrados
    contatos = {
        'contatos': Contato.objects.all()
    }
    
    return render(request, 'mensagens.html', contatos)


# pagina de sucesso
def pagina_sucesso(request):
    return render(request, 'sucesso.html')


# Processo os dados que vem do form
def inserir_contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST or None)
        
        # Todos os inputs serão obrigatórios
        if form: 
            #salvando os dados
            if form.is_valid():  
                form.save()
                # página de sucesso
                return redirect('sucesso')
        else:
            return HttpResponse("É obrigatória passar todos os dados do formulario!")
    else:
        form = ContatoForm()     
    
    return render(request, 'contato.html', {'form':form})


# Função para editar os nossos contatos
def editar_contato(request, contato_id):
    # Pegar contato especifico pelo id
    contato_especifico = Contato.objects.get(id=contato_id)
    
    form = ContatoForm(request.POST or None, instance=contato_especifico)
    
    if form.is_valid():  
        # Salvar novos dados do contato    
        contato_especifico.save()
        return redirect('mensagens')
    
    else:
        return render(request, 'contato.html', {'form':form,'contato_especifico':contato_especifico})


# tela que encaminha para deletar contato específico
def tela_deletar_contato(request, contato_id):
    
    contato_especifico =  Contato.objects.get(id=contato_id)
    print(f'Esse é o id:{contato_especifico}')
    return render(request, 'deletar_contato.html', {'contato':contato_especifico})


# view que de fato irá deletar o contato
def deletar_contato(request, contato_id):
    
    # pegando contato específico
    contato_cadastrado = Contato.objects.get(id=contato_id)
    print(f'Esse é o id:{contato_cadastrado}')
    
    # if request.method == 'POST':
    contato_cadastrado.delete()
    # Redirecionar para a lista de contatos após a exclusão
    return redirect('mensagens')
    
    # return render(request, 'deletar_contato.html', {'contato':contato_cadastrado})