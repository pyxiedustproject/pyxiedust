from django.shortcuts import render


def home(request):
    """
    The view for the homepage of the website.
    We simply "render" (display) the template called "home.html"
    """
    return render(request, 'home.html')
