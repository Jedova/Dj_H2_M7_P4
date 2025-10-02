from django import forms
from .models import Inmueble

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ["direccion", "comuna", "tipo", "descripcion", "precio_mensual", "disponible"]
