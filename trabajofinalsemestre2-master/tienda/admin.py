# tienda/admin.py
from django.contrib import admin
from .models import Zapato

@admin.register(Zapato)
class ZapatoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','marca','precio','tipo','talla','puntuacion','creado')
    list_display_links = ('nombre',)
    search_fields = ('nombre','marca','tipo')
    list_filter = ('marca','tipo')
