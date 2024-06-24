# events/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.evento_list, name='evento_list'),  # Lista de eventos
    path('create/', views.evento_create, name='create_event'),  # Criar evento
    path('update/<int:pk>/', views.evento_update, name='update_event'),
    path('delete/<int:pk>/', views.evento_delete, name='delete_event'),
]

