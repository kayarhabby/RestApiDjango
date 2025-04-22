from django.urls import path, include
from . import views
from .views import IndexTemplateView, CityTileView

app_name = 'RestApi'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('api/', include('RestApi.urls_api')),
    path('team/', views.TeamListView.as_view(), name='team'),
    path('cityLeaflet/', views.CityLeafletView.as_view(), name='cityLeaflet'),
    path('cityMapLibre/', views.CityMapLibreView.as_view(), name='cityMapLibre'),
    path('segmentRoutier/', views.RoadSegmentTemplateView.as_view(), name='segmentRoutier'),

    path('cities/', views.CityTileView.as_view(), name='citiesTiles'),

    path('books/', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),

    path('authors/', views.AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),

     #path("tiles/cities/<int:z>/<int:x>/<int:y>.pbf", CityTileView.as_view(), name="city_tiles"),

]