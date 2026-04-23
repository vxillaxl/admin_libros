from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import AutorForm, LibroForm
from .models import Autor, Libro


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


# --- Libros: vistas basadas en clases (List, Create, Update, Delete) ---


class LibroListView(ListView):
    model = Libro
    template_name = "gestion/lista_libros.html"
    context_object_name = "libros"


class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = "gestion/libro_form.html"
    success_url = reverse_lazy("lista_libros")


class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = "gestion/libro_form.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("lista_libros")


class LibroDeleteView(DeleteView):
    model = Libro
    template_name = "gestion/libro_confirm_delete.html"
    context_object_name = "libro"
    success_url = reverse_lazy("lista_libros")
