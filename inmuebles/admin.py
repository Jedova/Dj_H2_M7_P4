from django.contrib import admin
from .models import Region, Comuna, Inmueble

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)

@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "region")
    search_fields = ("nombre", "region__nombre")
    list_filter = ("region",)

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ("id", "direccion", "comuna", "region", "precio_mensual", "disponible")
    search_fields = ("direccion", "comuna__nombre", "comuna__region__nombre")
    list_filter = ("disponible", "comuna", "comuna__region")

    def region(self, obj):
        return obj.comuna.region
    region.admin_order_field = "comuna__region__nombre"
    region.short_description = "Región"

# Branding opcional:
admin.site.site_header = "Administración de Inmuebles"
admin.site.site_title  = "Panel Inmuebles"
admin.site.index_title = "Gestión de datos"
