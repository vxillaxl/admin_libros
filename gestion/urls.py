from django.urls import path

from . import views

# 8 URLs: 4 vistas por función (Autores) + 4 vistas por clase (Libros)
urlpatterns = [
    path("autores/", views.lista_autores, name="lista_autores"),
    path("autores/crear/", views.crear_autor, name="crear_autor"),
    path("autores/editar/<int:pk>/", views.editar_autor, name="editar_autor"),
    path(
        "autores/eliminar/<int:pk>/",
        views.eliminar_autor,
        name="eliminar_autor",
    ),
    path("libros/", views.LibroListView.as_view(), name="lista_libros"),
    path("libros/crear/", views.LibroCreateView.as_view(), name="crear_libro"),
    path(
        "libros/editar/<int:pk>/",
        views.LibroUpdateView.as_view(),
        name="editar_libro",
    ),
    path(
        "libros/eliminar/<int:pk>/",
        views.LibroDeleteView.as_view(),
        name="eliminar_libro",
    ),
]
