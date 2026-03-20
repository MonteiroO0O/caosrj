from django.shortcuts import render
from .models import CategoriaStaff, CalendarioGuerra, NoticiaJornal

def home(request):
    # Pega as categorias, guerras ativas e as últimas 6 notícias
    categorias = CategoriaStaff.objects.prefetch_related('membrostaff_set').all()
    guerras = CalendarioGuerra.objects.filter(ativo=True).order_by('dia_semana', 'horario')
    noticias = NoticiaJornal.objects.all().order_by('-data_publicacao')[:6]
    
    context = {
        'categorias': categorias,
        'guerras': guerras,
        'noticias': noticias,
    }
    return render(request, 'index.html', context)