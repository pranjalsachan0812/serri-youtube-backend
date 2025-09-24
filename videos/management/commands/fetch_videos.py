import time
from django.core.management.base import BaseCommand
from videos.youtube_fetcher import fetch_latest_videos

class Command(BaseCommand):
    help = 'Continuously fetch latest YouTube videos'

    def handle(self, *args, **kwargs):
        while True:
            fetch_latest_videos()
            self.stdout.write('Fetched latest videos')
            time.sleep(10)
