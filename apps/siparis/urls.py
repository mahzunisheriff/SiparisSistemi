from rest_framework.routers import DefaultRouter
from .views import SiparisViewSet, urun_siparis_olustur
from django.urls import path, include
router = DefaultRouter()

router.register(r'siparis', SiparisViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('urun_siparis_olustur/', urun_siparis_olustur, name='urun-siparis-olustur'),
]