# tienda/templatetags/product_tags.py
from django import template
from tienda.models import Zapato

register = template.Library()

@register.inclusion_tag('tienda/_productos_grid.html', takes_context=False)
def mostrar_productos(limit=12):
    """
    inclusion_tag que devuelve 'zapatos' para renderizar _productos_grid.html
    uso en plantilla: {% mostrar_productos 8 %}  (8 productos)
    """
    try:
        limit = int(limit)
    except (ValueError, TypeError):
        limit = 12
    productos = Zapato.objects.all().order_by('-creado')[:limit]  # si no tienes 'creado', usa .all()
    return {'zapatos': productos}
