from rest_framework import serializers
from .models import ParkingSpot


class SpotSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source='user.phone', required=False)
    email = serializers.CharField(source='user.email', required=False)

    class Meta:
        model = ParkingSpot
        fields = ('user', 'id', 'email', 'phone', 'description', 'price', 'image', 'available', 'longitude', 'latitude')
