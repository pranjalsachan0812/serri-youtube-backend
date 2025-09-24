from django.urls import path
from .views import VideoSearchAPIView

urlpatterns = [
    path('videos/search/', VideoSearchAPIView.as_view(), name='video-search'),
]
