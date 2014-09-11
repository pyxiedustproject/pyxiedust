from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    deadline = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def is_urgent(self):
        if not self.deadline:
            return False
        today = timezone.now()
        return today > self.deadline
