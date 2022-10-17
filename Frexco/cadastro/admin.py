from django.contrib import admin
from .models import Cadastro


class CadastrosAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'senha', 'data_de_nascimento')
    list_display_links = ('id', 'login')
    list_filter = ('login', )
    list_per_page = 10
    search_fields = ('id', 'login')


admin.site.register(Cadastro, CadastrosAdmin)
