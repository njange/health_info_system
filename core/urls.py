from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProgramViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'programs', ProgramViewSet, basename='program')

urlpatterns = [
    path('', include(router.urls)),
]
