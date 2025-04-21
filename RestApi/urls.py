from django.urls import path, include
from . import views
from .views import IndexTemplateView

app_name = 'RestApi'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('api/', include('RestApi.urls_api')),
    path('team/', views.TeamListView.as_view(), name='team'),
    path('cityLeaflet/', views.CityLeafletView.as_view(), name='cityLeaflet'),
    path('cityMapLibre/', views.CityMapLibreView.as_view(), name='cityMapLibre'),
    path('segmentRoutier/', views.RoadSegmentTemplateView.as_view(), name='segmentRoutier'),
]