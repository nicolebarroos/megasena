from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from game import views

urlpatterns = [
    path('plays/', views.play_list),
    path('generate_dozens/', views.generate_dozens),
    path('play_game/', views.play_game),
    path('play/<int:pk>', views.plays_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)