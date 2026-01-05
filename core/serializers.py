from rest_framework import serializers
from .models import Kala


class KalaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kala
        fields = "__all__"
