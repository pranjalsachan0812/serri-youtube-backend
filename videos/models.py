from django.db import models

class Video(models.Model):
    video_id = models.CharField(max_length=128, unique=True, db_index=True)
    title = models.TextField(db_index=True)
    description = models.TextField(db_index=True)
    published_at = models.DateTimeField(db_index=True)
    thumbnail_url = models.URLField(null=True)
    channel_title = models.CharField(max_length=256, null=True, db_index=True)

    def __str__(self):
        return self.title
