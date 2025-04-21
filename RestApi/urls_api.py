from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, RoadViewSet
from .views import CityViewSet

router = DefaultRouter()
router.register(r'team', TeamViewSet, basename='team')
router.register(r'city', CityViewSet, basename='city')
router.register(r'roads', RoadViewSet, basename='road')

router.register(r'segments', RoadViewSet, basename='road-segment')
urlpatterns = router.urls