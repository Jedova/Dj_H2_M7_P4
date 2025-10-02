# inmuebles/models.py
from django.db import models

class Region(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    class Meta: ordering = ["nombre"]
    def __str__(self): return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=120)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="comunas")
    class Meta:
        unique_together = (("nombre", "region"),)
        ordering = ["region__nombre", "nombre"]
    def __str__(self): return f"{self.nombre} ({self.region})"

class TipoInmueble(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    class Meta: ordering = ["nombre"]
    def __str__(self): return self.nombre

class Inmueble(models.Model):
    direccion = models.CharField(max_length=200)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT, related_name="inmuebles")
    tipo = models.ForeignKey(TipoInmueble, on_delete=models.PROTECT, related_name="inmuebles", null=True, blank=True)
    descripcion = models.TextField(blank=True)         # ← para “descripción”
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    class Meta:
        ordering = ["comuna__region__nombre", "comuna__nombre", "direccion"]
    def __str__(self):
        return f"{self.direccion} - {self.comuna} (${self.precio_mensual})"
