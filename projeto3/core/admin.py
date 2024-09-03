from django.contrib import admin
from .models import Cargo, Servico, Funcionario, Feature


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'mod_obj')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'mod_obj')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'mod_obj')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'icone', 'mod_obj')