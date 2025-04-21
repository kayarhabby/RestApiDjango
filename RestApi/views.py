from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

from rest_framework import viewsets
from .models import Team, City, Road
from .serializers import TeamSerializer, CitySerializer, RoadSerializer


# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = 'index.html'

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamListView(TemplateView):
    template_name = 'team.html'

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityLeafletView(TemplateView):
    template_name = 'cityLeaflet.html'

class CityMapLibreView(TemplateView):
    template_name = 'cityMaplibre.html'

class RoadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer

class RoadSegmentTemplateView(TemplateView):
    template_name = 'segmentRoutier.html'