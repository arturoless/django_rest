# -------------AGREGANDO LIBRERIAS FRAMEWORK-----------
from rest_framework import routers, serializers, viewsets

# -------------AGREGANDO MODELOS-----------------
from example.models import Example,Person

class ExampleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('__all__')

class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')

