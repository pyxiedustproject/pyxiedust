from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=200)
    recipe = models.TextField(blank=True)
    score = models.IntegerField(default=50)

    def __str__(self):
        return self.name
