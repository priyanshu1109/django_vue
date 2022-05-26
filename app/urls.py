from django.urls import include, path
from rest_framework import routers
from app.views import VueViewSet


urlpatterns = [
    path('', VueViewSet.as_view(), name="main"),
]