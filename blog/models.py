from django.db import models
from django.utils import timezone

# Here we define the "Post" model which is the object that will store all the
# information.
# The first lines define the "fields" which are all the different types of
# information we want to store.
# If you add, change, or delete some fields, don't forget to run:
# python manage.py makemigrations
# python manage.py migrate
# heroku run python manage.py migrate

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        """
        Show the title of the post instead of an ugly
        <Article object at 0x7f93799d3f98>
        """
        return self.title

    def publish(self):
        """
        Publish the post by putting the current date/time in the
        published_date field.
        """
        self.date_published = timezone.now()
        self.save()

    def unpublish(self):
        """
        Un-publish the post so that it doesn't appear on the site.
        """
        self.date_published = None
        self.save()
