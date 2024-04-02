from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'rua','bairro', 'cidade', 'uf', 'cep', 'email', 'numero']

        