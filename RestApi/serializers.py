from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Team, City, Road

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        # fields = ['id', 'name', 'image', 'created_at']
        # exclude = ['created_at']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        # fields = ['id', 'name', 'population', 'image', 'location', 'created_at']
        # exclude = ['created_at']

class RoadSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Road
        geo_field = "geometry"
        fields = ("id", "name")