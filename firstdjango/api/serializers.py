from rest_framework import serializers
from authentication import models


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'user',
            'password',
        )
        model = models.Usuario