from django.shortcuts import render, redirect, get_object_or_404
from .models import Contato

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


def contato(request):
    
    mensagem = {'mensagem':"Formulário"}
    
    return render(request, 'contato.html', mensagem)

# pagina de sucesso
def pagina_sucesso(request):
    return render(request, 'sucesso.html')


def inserir_contato(request):
    if request.method == 'POST':
        # passando os dados capturados no form
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        email = request.POST['email']
        mensagem = request.POST['mensagem']
        
        # instanciando 
        contato_form = Contato(nome=nome, telefone=telefone, email=email, mensagem=mensagem)
        
        if contato_form.is_valid():
            
            contato_form.save()
            # página de sucesso
            return redirect('sucesso')
        
    
    return render(request, 'contato.html')

# Função para editar os nossos contatos
def editar_contato(request, contato_id):
    # Pegar contato especifico pelo id
    contato_especifico = Contato.objects.get(id=contato_id)
    
    if request.method == 'POST':
        # Processar dados aqui
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        email = request.POST["email"]
        mensagem = request.POST['mensagem']
        
        # Atualizar os campos do form
        contato_especifico.nome = nome
        contato_especifico.telefone = telefone
        contato_especifico.email = email
        contato_especifico.mensagem = mensagem
        
        # Salvar novos dados do contato
        if contato_especifico.is_valid():
            
            contato_especifico.save()
            return redirect('mensagens', contato_id=contato_id)
    
    return render(request, 'contato.html', {'contato_especifico':contato_especifico})

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