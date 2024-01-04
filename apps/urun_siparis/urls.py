from rest_framework.routers import DefaultRouter
from .views import UrunSiparisViewSet
from django.urls import path, include
router = DefaultRouter()

router.register(r'musteri', UrunSiparisViewSet)

urlpatterns = [
    path('', include(router.urls))
]