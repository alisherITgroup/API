from django.urls import path
from .viewsets import AttemptViewSet
from rest_framework.routers import DefaultRouter

rounter = DefaultRouter()
rounter.register("", AttemptViewSet)

urlpatterns = [
    
]

urlpatterns += rounter.urls