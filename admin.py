from django.contrib import admin
from .models import CategoriaStaff, MembroStaff, NoticiaJornal, CalendarioGuerra

admin.site.register(CategoriaStaff)

@admin.register(MembroStaff)
class MembroStaffAdmin(admin.ModelAdmin):
    # Aqui permite que você veja e pesquise rápido no painel
    list_display = ('nick', 'categoria', 'cargo_especifico')
    list_filter = ('categoria',)
    search_fields = ('nick',)

@admin.register(NoticiaJornal)
class NoticiaJornalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao', 'autor')

@admin.register(CalendarioGuerra)
class CalendarioGuerraAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'dia_semana', 'horario', 'ativo')
    list_filter = ('dia_semana', 'ativo')