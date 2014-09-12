from django.conf import settings
from django.contrib.auth.views import redirect_to_login


class LoginRequiredMiddleware(object):
    """
    If this middleware is installed, all pages on the website will be protected
    and will require the visitor to log in to view them.
    """
    def process_request(self, request):
        assert hasattr(request, 'user')
        if request.user.is_authenticated():
            return None  # OK, you're allowed

        if request.path == settings.LOGIN_URL:
            return None  # Don't block the login page

        current_page = request.build_absolute_uri()
        return redirect_to_login(current_page)
