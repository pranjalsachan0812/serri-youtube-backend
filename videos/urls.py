from django.urls import path
from .views import VideoListView, VideoSearchAPIView

urlpatterns = [
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('videos/search/', VideoSearchAPIView.as_view(), name='video-search'),
]
