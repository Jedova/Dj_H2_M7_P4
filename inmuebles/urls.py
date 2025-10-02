from django.urls import path
from .views import listar_inmuebles, listar_propios, crear_inmueble, editar_inmueble, eliminar_inmueble

app_name = "inmuebles"

urlpatterns = [
    path("oferta/", listar_inmuebles, name="listar"),
    path("gestionar/", listar_propios, name="listar_propios"),
    path("nuevo/", crear_inmueble, name="crear"),
    path("<int:pk>/editar/", editar_inmueble, name="editar"),
    path("<int:pk>/eliminar/", eliminar_inmueble, name="eliminar"),
]

