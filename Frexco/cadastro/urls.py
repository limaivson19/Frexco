from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cadastro_id>', views.ver_usuario, name='ver_usuario'),
    path('cadastrar_user', views.cadastrar_user, name='cadastrar_user'),
]
