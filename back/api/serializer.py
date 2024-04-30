from rest_framework import serializers
from .models import Cliente
from django.contrib.auth.models import User

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'rua','bairro', 'cidade', 'uf', 'cep', 'email', 'numero', 'image']

class UserSerializar(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user