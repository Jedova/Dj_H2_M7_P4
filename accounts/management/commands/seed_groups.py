from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = "Crea grupos y asigna permisos"

    def handle(self, *args, **opts):
        # Ajusta a modelos reales
        Inmueble = apps.get_model("inmuebles", "Inmueble")

        # Permisos por codename 
        perms_agente = [
            Permission.objects.get(codename=f"view_{Inmueble._meta.model_name}"),
            Permission.objects.get(codename=f"add_{Inmueble._meta.model_name}"),
            Permission.objects.get(codename=f"change_{Inmueble._meta.model_name}"),
        ]
        perms_arrendatario = [
            Permission.objects.get(codename=f"view_{Inmueble._meta.model_name}"),
        ]

        agente, _ = Group.objects.get_or_create(name="Agente")
        agente.permissions.set(perms_agente)

        arrendatario, _ = Group.objects.get_or_create(name="Arrendatario")
        arrendatario.permissions.set(perms_arrendatario)

        self.stdout.write(self.style.SUCCESS("Grupos y permisos creados/actualizados"))
