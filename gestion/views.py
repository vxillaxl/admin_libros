from django.shortcuts import get_object_or_404, redirect, render

from .forms import AutorForm
from .models import Autor


def lista_autores(request):
    """Leer / listar autores."""
    autores = Autor.objects.all()
    return render(request, "gestion/lista_autores.html", {"autores": autores})


def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_autores")
    else:
        form = AutorForm()
    return render(request, "gestion/autor_form.html", {"form": form})


def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect("lista_autores")
    else:
        form = AutorForm(instance=autor)
    return render(request, "gestion/autor_form.html", {"form": form, "object": autor})


def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        autor.delete()
        return redirect("lista_autores")
    return render(request, "gestion/autor_confirm_delete.html", {"autor": autor})
