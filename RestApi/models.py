from django.db import models
from django.contrib.gis.db import models as geomodels
# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="api/team/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    image = models.ImageField(upload_to="api/city/", null=True, blank=True)
    location = geomodels.PointField() # Using PointField for storing geographical coordinates
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Road(models.Model):
    name = models.CharField(max_length=100)
    geometry = geomodels.LineStringField(srid=4326)

    def __str__(self):
        return self.name

class RoadSegment(models.Model):
    road = models.ForeignKey(Road, on_delete=models.CASCADE, related_name="segments")
    start_km = models.FloatField()
    end_km = models.FloatField()
    status = models.CharField(max_length=100, choices=[
        ("good", "Bon état"),
        ("works", "En travaux"),
        ("slow", "Limitation de vitesse")
    ])

    def __str__(self):
        return f"{self.road.name} [{self.start_km} km → {self.end_km} km] - {self.status}"


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title

