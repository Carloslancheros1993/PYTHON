from django.contrib import admin
from django.urls import path
from estudiantes.views import vista_estudiantes, detalle_estudiante
from profesores.views import vista_profesores

app_name = 'estudiantes'
urlpatterns = [
    path('', vista_estudiantes, name="list"),
    path('<int:estudiante_id>/', detalle_estudiante, name='detail')
]