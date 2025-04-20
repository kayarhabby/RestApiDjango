from django.urls import path
from . import views
from .views import IndexTemplateView

app_name = 'RestApi'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('team/', views.TeamViewSet.as_view({'get': 'list'}), name='team-list'),
]