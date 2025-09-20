from rest_framework import serializers
from .models import Zapato

class ZapatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zapato
        fields = '__all__'