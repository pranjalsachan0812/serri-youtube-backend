from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Video
from .serializers import VideoSerializer

class VideoSearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        if not query:
            return Response({"error": "Query parameter 'q' is required."}, status=status.HTTP_400_BAD_REQUEST)
        # Split query for partial matching of any words
        query_words = query.split()
        q_objects = Q()
        for word in query_words:
            q_objects |= Q(title__icontains=word) | Q(description__icontains=word)

        videos = Video.objects.filter(q_objects).order_by('-published_at')
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
