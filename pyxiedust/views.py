from django.shortcuts import render


def home(request):
    """
    The view for the homepage of the website.
    """
    return render(request, 'home.html')
