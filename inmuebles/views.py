from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Inmueble
from .forms import InmuebleForm
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

def es_arrendador(user):
   
    return user.is_staff or user.groups.filter(name__in=["Agente", "Arrendador"]).exists()


def listar_inmuebles(request):
    
    qs = Inmueble.objects.filter(disponible=True).select_related("comuna", "comuna__region", "tipo").order_by(
        "comuna__region__nombre", "comuna__nombre", "direccion"
    )
    return render(request, "inmuebles/listar.html", {"inmuebles": qs})


@login_required
@user_passes_test(es_arrendador)
def crear_inmueble(request):
    if request.method == "POST":
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save()  
            messages.success(request, "Inmueble creado.")
            return redirect("inmuebles:listar_propios")
    else:
        form = InmuebleForm()
    return render(request, "inmuebles/crear.html", {"form": form})


@login_required
@user_passes_test(es_arrendador)
def editar_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)  
    if request.method == "POST":
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()  
            messages.success(request, "Inmueble actualizado.")
            return redirect("inmuebles:listar_propios")
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, "inmuebles/editar.html", {"form": form, "inmueble": inmueble})


@login_required
@user_passes_test(es_arrendador)
def eliminar_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    if request.method == "POST":
        inmueble.delete()  
        messages.success(request, "Inmueble eliminado.")
        return redirect("inmuebles:listar_propios")
    return render(request, "inmuebles/eliminar_confirm.html", {"inmueble": inmueble})


@login_required
@user_passes_test(es_arrendador)
def listar_propios(request):
    qs = Inmueble.objects.all().select_related("comuna", "comuna__region", "tipo").order_by("-id")
    return render(request, "inmuebles/listar_propios.html", {"inmuebles": qs})

@permission_required("inmuebles.view_inmueble", raise_exception=True)
def solo_lectura_inmuebles(request):
    return HttpResponse("<h1>Listado (solo lectura)</h1>")