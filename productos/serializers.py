from productos.models import Productos 
from rest_framework import serializers


class ProductosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = "__all__"
