from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Team, City, Road, RoadSegment, Author, Book

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

class RoadSegmentSerializer(GeoFeatureModelSerializer):
    road = RoadSerializer()

    class Meta:
        model = RoadSegment
        fields = ['id', 'road', 'start_km', 'end_km', 'status']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'