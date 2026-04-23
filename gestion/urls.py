from django.urls import path

from . import views

urlpatterns = [
    path("autores/", views.lista_autores, name="lista_autores"),
    path("autores/crear/", views.crear_autor, name="crear_autor"),
    path("autores/editar/<int:pk>/", views.editar_autor, name="editar_autor"),
    path(
        "autores/eliminar/<int:pk>/",
        views.eliminar_autor,
        name="eliminar_autor",
    ),
]
