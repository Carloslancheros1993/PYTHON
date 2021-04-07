from django.http import HttpResponse
from django.shortcuts import render, redirect

from estudiantes.models import Estudiante

def vista_estudiantes(request):
    if request.method == 'GET':
        estudiantes = Estudiante.objects.all()
        contexto = {
        'estudiantes': estudiantes
        }
        return render(request, 'estudiantes/lista.html', contexto)

    if request.method == 'POST':
        Estudiante.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            edad=request.POST['edad'],
            telefono=request.POST['telefono']
        )
        estudiantes = Estudiante.objects.all()
        contexto = {
            'estudiantes': estudiantes
        }
        return render(request, 'estudiantes/lista.html', contexto)



def detalle_estudiante(request, estudiante_id):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    if request.method == "GET":
        contexto = {
            'estudiante': estudiante
        }
        return render(request, 'estudiantes/detalle.html', contexto)

    if request.method == "POST":
        print(estudiante)
        estudiante.delete()
        return redirect('estudiantes:list')