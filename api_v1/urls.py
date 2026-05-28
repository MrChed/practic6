from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomerViewSet,
    HallViewSet,
    MovieViewSet,
    SessionViewSet,
    TicketViewSet
)

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'halls', HallViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]