from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

@permission_required("inmuebles.view_inmueble", raise_exception=True)
def solo_lectura_inmuebles(request):
    return HttpResponse("<h1>Listado (solo lectura)</h1>")
