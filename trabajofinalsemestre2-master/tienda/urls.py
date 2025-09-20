from django.urls import path, include
from rest_framework import routers   # 👈 importa routers
from . import views

router = routers.DefaultRouter()
router.register(r'zapatos', views.ZapatoViewSet)

app_name = "tienda"

# Reorganiza tus URLs correctamente:
urlpatterns = [
    path('', views.lista_zapatos, name='lista_zapatos'),
    path('zapato/<int:pk>/', views.detalle_zapato, name='detalle_zapato'),
    path('panel/', views.panel, name='panel'),
    path('crear/', views.crear_zapato, name='crear_zapato'),
    path('editar/<int:pk>/', views.editar_zapato, name='editar_zapato'),
    path('eliminar/<int:pk>/', views.eliminar_zapato, name='eliminar_zapato'),

    # API
    path('api/', include(router.urls)),

    # Otras páginas
    path('contacto/', views.contacto, name='contacto'),
    path('carrito/', views.carrito, name='carrito'),
    path('perfil/', views.perfil, name='perfil'),
    path('sobre_nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('terminos/', views.terminos, name='terminos'),
    path('base/', views.base, name='base'),
    path('mis-pedidos/', views.mis_pedidos, name='mis_pedidos'),

]



















