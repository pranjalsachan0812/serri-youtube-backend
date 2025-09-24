import os
from datetime import datetime, timedelta, timezone
from googleapiclient.discovery import build
from dotenv import load_dotenv
from .models import Video

# Load environment variables from .env file
load_dotenv()

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
SEARCH_QUERY = 'cricket'


def fetch_latest_videos():
    if not YOUTUBE_API_KEY:
        raise ValueError("YouTube API key not found. Set YOUTUBE_API_KEY in your environment or .env file.")

    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    latest_video = Video.objects.order_by('-published_at').first()
    if latest_video:
        published_after = latest_video.published_at.isoformat()
        if not published_after.endswith('Z') and '+' not in published_after:
            published_after += 'Z'
    else:
        # Use timezone-aware datetime with 'Z'
        published_after = (datetime.now(timezone.utc) - timedelta(days=1)).replace(microsecond=0).isoformat()

    request = youtube.search().list(
        q=SEARCH_QUERY,
        part='snippet',
        type='video',
        order='date',
        publishedAfter=published_after,
        maxResults=5
    )
    response = request.execute()

    for item in response.get('items', []):
        video_id = item['id']['videoId']
        snippet = item['snippet']
        Video.objects.update_or_create(
            video_id=video_id,
            defaults={
                'title': snippet['title'],
                'description': snippet['description'],
                'published_at': snippet['publishedAt'],
                'thumbnail_url': snippet['thumbnails']['default']['url'],
                'channel_title': snippet['channelTitle'],
            }
        )
