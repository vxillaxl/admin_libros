from django import forms

from .models import Autor, Libro


class BootstrapFormMixin:
    """Asigna clases de Bootstrap a los widgets del formulario."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                widget.attrs.setdefault("class", "form-check-input")
            elif isinstance(widget, forms.Select):
                widget.attrs.setdefault("class", "form-select")
            else:
                widget.attrs.setdefault("class", "form-control")
            if isinstance(field, forms.DateField):
                widget.input_type = "date"


class AutorForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "correo", "nacionalidad", "fecha_nacimiento", "biografia"]


class LibroForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo", "fecha_publicacion", "genero", "isbn", "autor"]
