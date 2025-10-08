from django.shortcuts import render, redirect, get_object_or_404
from .models import MEDICO, ESPECIALIDADE

def home(request):
    medicos = MEDICO.objects.all() 
    especialidades = ESPECIALIDADE.objects.all()
    return render(request, 'home.html', {'medicos': medicos, 'especialidades':especialidades})

    
def deletar_usuario(request, id):
    usuario = get_object_or_404(MEDICO, id_medico=id)
    usuario.delete()
    return redirect('/home/')

def deletar_especialidade(request, id):
    usuario = get_object_or_404(ESPECIALIDADE, id_especialidade=id)
    usuario.delete()
    return redirect('/home/')

def editar_especialidade(request, id):
    usuario = get_object_or_404(ESPECIALIDADE, id_especialidade=id)
    if request.method == "POST":
        novo_nome = request.POST.get('nome')
        novo_descricao = request.POST.get('descricao')
        usuario.nome = novo_nome
        usuario.descricao = novo_descricao
        usuario.save()
        return redirect('/home/')
    
    return render(request, 'editar_especialidade.html', {'usuario': usuario})

def editar_medico(request, id):
    medico = get_object_or_404(MEDICO, id_medico=id)
    especialidades = ESPECIALIDADE.objects.all()

    if request.method == "POST":
        medico.nome = request.POST.get('nome')
        medico.endereco = request.POST.get('endereco')
        medico.telefone = request.POST.get('telefone')
        medico.email = request.POST.get('email')
        medico.data_nascimento = request.POST.get('data_nascimento')
        medico.crm = request.POST.get('crm')

        id_especialidade = request.POST.get('id_especialidade')
        if id_especialidade:
            medico.id_especialidade = ESPECIALIDADE.objects.get(id_especialidade=id_especialidade)

        medico.save()
        return redirect('/home/')  # redireciona após salvar

    return render(request, 'editar_medico.html', {
        'medico': medico,
        'especialidades': especialidades
    })

def add_medico(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')
        crm = request.POST.get('crm')
        id_especialidade = request.POST.get('id_especialidade')
        especialidade = ESPECIALIDADE.objects.get(id_especialidade=id_especialidade)

        user = MEDICO(
            nome=nome,
            endereco=endereco,
            telefone=telefone,
            email=email,
            data_nascimento=data_nascimento,
            crm=crm,
            id_especialidade=especialidade
        )
        user.save()
        return redirect('/home/')

    medicos = MEDICO.objects.all() 
    especialidades = ESPECIALIDADE.objects.all() 
    # especialidades = ESPECIALIDADE.objects.all()

    
    return render(request, 'adicionar_medico.html', {'medicos': medicos, 'especialidades':especialidades})
        

def add_especialidade(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')

        especialidade = ESPECIALIDADE(
            nome=nome,
            descricao=descricao,
        )

        especialidade.save()
        return redirect('/home/')

    medicos = MEDICO.objects.all() 
    especialidades = ESPECIALIDADE.objects.all() 
    # especialidades = ESPECIALIDADE.objects.all()

    
    return render(request, 'adicionar_especialidade.html', {'medicos': medicos, 'especialidades':especialidades})

