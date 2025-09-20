
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, BasePermission
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Zapato
from .serializers import ZapatoSerializer
from .forms import ZapatoForm
from django.shortcuts import render
# Asegúrate de tener esta importación al inicio:
from django.core.paginator import Paginator

class IsAdminOrReadOnly(BasePermission):
    """
    Permite GET/HEAD/OPTIONS a cualquiera, pero POST/PUT/DELETE solo a staff.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

class ZapatoViewSet(viewsets.ModelViewSet):
    """
    API REST para Zapato — puede usarse con DRF router.
    """
    queryset = Zapato.objects.all().order_by('-creado')
    serializer_class = ZapatoSerializer
    permission_classes = [IsAdminOrReadOnly]

# -- VISTAS HTML --
def contacto(request):
    # si tienes un template tienda/contacto.html úsalo, si no crea uno simple
    return render(request, 'tienda/contacto.html')

def lista_zapatos(request):
    """
    Página principal que muestra todos los zapatos en grid.
    """
    zapatos = Zapato.objects.all().order_by('-creado')
    return render(request, 'tienda/lista_zapatos.html', {'zapatos': zapatos})

def detalle_zapato(request, pk):
    """
    Detalle de un zapato (detail view).
    """
    zapato = get_object_or_404(Zapato, pk=pk)
    return render(request, 'tienda/detalle_zapato.html', {'zapato': zapato})

def is_staff_user(user):
    return user.is_active and user.is_staff

@user_passes_test(is_staff_user, login_url='/admin/login/?next=/panel/')
def panel(request):
    """
    Panel simple (solo accesible a staff) con listado y enlaces CRUD.
    """
    zapatos = Zapato.objects.all().order_by('-creado')
    return render(request, 'tienda/panel.html', {'zapatos': zapatos})

@user_passes_test(is_staff_user, login_url='/admin/login/?next=/panel/')
def crear_zapato(request):
    """
    Form para crear un zapato (usa ZapatoForm, soporta imagenes con request.FILES).
    """
    if request.method == 'POST':
        form = ZapatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tienda:panel')
    else:
        form = ZapatoForm()
    return render(request, 'tienda/zapato_form.html', {'form': form})

@user_passes_test(is_staff_user, login_url='/admin/login/?next=/panel/')
def editar_zapato(request, pk):
    zapato = get_object_or_404(Zapato, pk=pk)
    if request.method == 'POST':
        form = ZapatoForm(request.POST, request.FILES, instance=zapato)
        if form.is_valid():
            form.save()
            return redirect('tienda:panel')
    else:
        form = ZapatoForm(instance=zapato)
    return render(request, 'tienda/zapato_form.html', {'form': form, 'zapato': zapato})

@user_passes_test(is_staff_user, login_url='/admin/login/?next=/panel/')
def eliminar_zapato(request, pk):
    zapato = get_object_or_404(Zapato, pk=pk)
    if request.method == 'POST':
        zapato.delete()
        return redirect('tienda:panel')
    return render(request, 'tienda/confirm_delete.html', {'zapato': zapato})













def carrito(request):
    return render(request, 'tienda/carrito.html')

def contacto(request):
    return render(request, 'tienda/contacto.html')

def terminos(request):
    return render(request, 'tienda/terminos.html')

def sobre_nosotros(request):
    return render(request, 'tienda/sobre_nosotros.html')

def perfil(request):
    return render(request, 'tienda/perfil.html')

def base(request):
    return render(request, 'tienda/base.html')

def mis_pedidos(request):
    return render(request, 'mis_pedidos.html')











