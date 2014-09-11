from django.shortcuts import get_object_or_404, render

from .models import Post

def post_list(request):
    """
    Display all the blog posts.
    """
    # Only show the posts that have been published
    posts = Post.objects.filter(date_published__isnull=False)
    return render(request,
        'blog/post_list.html',
        {'posts': posts}
    )


def post_detail(request, post_id):
    """
    Display a page with only one post.
    """
    post = get_object_or_404(Post, id=post_id)
    return render(request,
        'blog/post_detail.html',
        {'post': post}
    )
