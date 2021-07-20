from django.urls import path, include
from rest_framework import routers

from game.views import PLaysViewSet

router = routers.DefaultRouter()

router.register(r'plays', PLaysViewSet)


urlpatterns = [
    path('', include(router.urls)),

]