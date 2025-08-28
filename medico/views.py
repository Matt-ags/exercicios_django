from django.shortcuts import render, redirect, get_object_or_404
from .models import MEDICO, ESPECIALIDADE

def home(request):
    medicos = MEDICO.objects.all() 
    especialidades = ESPECIALIDADE.objects.all()
    return render(request, 'home.html', {'medicos': medicos, 'especialidades':especialidades})

    
def deletar_usuario(request, id):
    usuario = get_object_or_404(MEDICO, id=id)
    usuario.delete()
    return redirect('/home/')

def deletar_especialidade(request, id):
    usuario = get_object_or_404(ESPECIALIDADE, id=id)
    usuario.delete()
    return redirect('/home/')

# Create your views here.
