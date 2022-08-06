from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Noticia, Categoria
# Create your views here.

class AddNoticia(CreateView):
    model = Noticia
    fields = ['titulo', 'texto', 'categoria', 'activo', 'imagen']
    template_name = 'noticia/addNoticia.html'
    success_url = reverse_lazy('index')

# vista de edicion generica basada en clase
class mostrarNoticia(ListView):
    model = Noticia
    template_name = 'noticia/listarNoticia.html'

# vista de edicion generica basada en funciones
def ListarNoticia(request):
    noticia = Noticia.objects.all()
    context = {
		'noticia': noticia,
	}
    return render(request, 'noticia/listarNoticia2.html', context)

def ListarNoticiaPorCategoria(request, categoria):
    categoria2 = Categoria.objects.filter(nombre=categoria)

    noticia = Noticia.objects.filter(categoria = categoria2[0].id)
    context = { 
		'noticia': noticia,
    }
    return render(request,'noticia/listarNoticia2.html', context)