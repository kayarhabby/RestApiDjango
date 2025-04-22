from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

from rest_framework import viewsets, request, status, generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from vectortiles.rest_framework.renderers import MVTRenderer
from vectortiles.views import BaseVectorTileView

from .models import Team, City, Road, Book, Author, RoadSegment
from .serializers import TeamSerializer, CitySerializer, RoadSerializer, BookSerializer, AuthorSerializer


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

class RoadSegmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RoadSegment.objects.all()
    serializer_class = RoadSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        road_id = self.request.query_params.get('road_id')
        if road_id:
            queryset = queryset.filter(road__id=road_id)
        return queryset


class RoadSegmentTemplateView(TemplateView):
    template_name = 'segmentRoutier.html'

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# City model tile
class CityTileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    id = "cities"
    tile_fields = ("name", "population")
    queryset_limit = 500

class CityTileView(TemplateView):
    template_name = 'cityTile.html'