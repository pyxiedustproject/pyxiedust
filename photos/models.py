import os

from django.db import models
from django.utils import timezone


class Photo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to=os.getenv('AWS_BUCKET_FOLDER', ''))
    date_uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title or '<no title>'
