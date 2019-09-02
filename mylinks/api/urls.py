from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets


router = DefaultRouter()
router.register(r'content', viewsets.ContentViewSet, base_name='content')
router.register(r'link', viewsets.LinkViewSet, base_name='link')

urlpatterns = [
    path(r'', include(router.urls)),
]
