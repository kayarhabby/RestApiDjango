from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, RoadViewSet, RoadSegmentViewSet, CityTileViewSet, CityViewSet

router = DefaultRouter()
router.register(r'team', TeamViewSet, basename='team')
router.register(r'city', CityViewSet, basename='city')
router.register(r'roads', RoadViewSet, basename='road')

router.register(r'segments', RoadSegmentViewSet, basename='road-segment')
router.register(r'tiles', CityTileViewSet, basename='tiles')
urlpatterns = router.urls