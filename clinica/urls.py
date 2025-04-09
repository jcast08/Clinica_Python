from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.shortcuts import redirect

urlpatterns = [
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('editar-historial/', views.editar_historial, name='editar_historial'),
    path('buscar-pacientes/', views.buscar_pacientes, name='buscar_pacientes'),
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('', lambda request: redirect('login/')),
]
