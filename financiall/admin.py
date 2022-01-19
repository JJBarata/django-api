from django.contrib import admin
from financiall.models import Receita, Despesa

class Receitas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao', 'valor', 'data')
    list_filter = ('id','descricao','data', 'valor',)
    search_fields = ('descricao', 'valor', 'data',)

admin.site.register(Receita, Receitas)

class Despesas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao', 'valor', 'data')
    list_filter = ('id','descricao','data', 'valor',)
    search_fields = ('descricao', 'valor', 'data',)

admin.site.register(Despesa, Despesas)
