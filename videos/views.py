from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer

class VideoListView(generics.ListAPIView):
    queryset = Video.objects.order_by('-published_at')
    serializer_class = VideoSerializer
