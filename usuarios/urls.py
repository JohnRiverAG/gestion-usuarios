# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('lista/', views.lista_usuarios, name='lista'),
    path('editar/<int:usuario_id>/', views.editar_usuario, name='editar'),
    path('eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar'),
]
