from django.contrib import admin

from .models import Post

admin.site.register(Post)  # This will allow us to manage blog posts in the Django admin page
