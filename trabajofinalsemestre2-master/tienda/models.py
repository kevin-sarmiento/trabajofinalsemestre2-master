from django.db import models

class Zapato(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    talla = models.CharField(max_length=20)
    marca = models.CharField(max_length=100)
    puntuacion = models.FloatField(default=0.0)

    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  # opcional
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - {self.marca} ({self.talla})"
