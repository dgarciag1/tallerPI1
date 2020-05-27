from rest_framework import serializers
from .models import Luminosity

class LuminositySerializer(serializers.ModelSerializer):
    class Meta:
        model = Luminosity
        fields = ('id', 'type', 'value')