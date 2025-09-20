# tienda/context_processors.py
from .models import Zapato

def productos_destacados(request):
    # Devuelve un queryset o lista para usar en todas las plantillas
    productos = Zapato.objects.all().order_by('-creado')[:20]   # ajusta el número
    return {'productos_destacados': productos}
