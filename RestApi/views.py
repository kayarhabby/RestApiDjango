from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

from rest_framework import viewsets
from .models import Team
from .serializers import TeamSerializer

# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = 'index.html'

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
