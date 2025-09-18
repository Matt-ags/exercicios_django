
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
    usuario_medico = get_object_or_404(MEDICO, id_medico=id)
    especialidades = ESPECIALIDADE.objects.all()
    if request.method == "POST":
        novo_nome = request.POST.get('nome')
        novo_telefone = request.POST.get('telefone')
        novo_email = request.POST.get('email')
        novo_data_nascimento = request.POST.get('data_nascimento')
        novo_crm = request.POST.get('crm')
        novo_especialidade = request.POST.get('id_especialidade')

        usuario_medico.nome = novo_nome
        usuario_medico.telefone = novo_telefone
        usuario_medico.email = novo_email
        usuario_medico.data_nascimento = novo_data_nascimento
        usuario_medico.crm = novo_crm
        usuario_medico.id_especialidade = novo_especialidade

        usuario_medico.save()
        return redirect('/home/')
    return render(request, 'editar_medico.html', {'usuario': usuario_medico}, {'especialidades': especialidades})


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


"""
"GABARITO":

forms.py
from django import forms
from .models import Especialidade, Medico

class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = ['nome', 'descricao']

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'endereco', 'telefone', 'email', 'data_nascimento', 'crm', 'especialidade']


views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Especialidade, Medico
from .forms import EspecialidadeForm, MedicoForm

class EspecialidadeListView(ListView):
    model = Especialidade
    template_name = 'especialidade_list.html'

class EspecialidadeCreateView(CreateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = 'especialidade_form.html'
    success_url = reverse_lazy('especialidade_list')

class EspecialidadeUpdateView(UpdateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = 'especialidade_form.html'
    success_url = reverse_lazy('especialidade_list')

class EspecialidadeDeleteView(DeleteView):
    model = Especialidade
    template_name = 'especialidade_confirm_delete.html'
    success_url = reverse_lazy('especialidade_list')

class MedicoListView(ListView):
    model = Medico
    template_name = 'medico_list.html'

class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico_form.html'
    success_url = reverse_lazy('medico_list')

class MedicoUpdateView(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico_form.html'
    success_url = reverse_lazy('medico_list')

class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'medico_confirm_delete.html'
    success_url = reverse_lazy('medico_list')


urls.py

from django.urls import path
from .views import (EspecialidadeListView, EspecialidadeCreateView, EspecialidadeUpdateView,
                    EspecialidadeDeleteView, MedicoListView, MedicoCreateView, MedicoUpdateView,
                    MedicoDeleteView)

urlpatterns = [
    path('especialidades/', EspecialidadeListView.as_view(), name='especialidade_list'),
    path('especialidades/create/', EspecialidadeCreateView.as_view(), name='especialidade_create'),
    path('especialidades/<int:pk>/update/', EspecialidadeUpdateView.as_view(), name='especialidade_edit'),
    path('especialidades/<int:pk>/delete/', EspecialidadeDeleteView.as_view(), name='especialidade_delete'),

    path('medicos/', MedicoListView.as_view(), name='medico_list'),
    path('medicos/create/', MedicoCreateView.as_view(), name='medico_create'),
    path('medicos/<int:pk>/update/', MedicoUpdateView.as_view(), name='medico_edit'),
    path('medicos/<int:pk>/delete/', MedicoDeleteView.as_view(), name='medico_delete'),
]

"""