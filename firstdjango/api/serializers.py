from rest_framework import serializers
from authentication import models


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'password',
        )
        model = models.Usuario
class UsuarioSigninSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)