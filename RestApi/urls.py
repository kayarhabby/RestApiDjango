from django.urls import path, include
from . import views
from .views import IndexTemplateView

app_name = 'RestApi'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('api/', include('RestApi.urls_api')),
]