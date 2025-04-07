from rest_framework import serializers
from .models import Livro

class LivroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'