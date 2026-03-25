from rest_framework import serializers
from .models import Travels

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travels
        fields = "__all__"
