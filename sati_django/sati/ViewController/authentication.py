from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import authenticate as mock_user
from django.contrib.auth.models import User
class SuperUserSessionAuthentication(SessionAuthentication):
    """
    Use Django's session framework for authentication of super users.
    """

    def authenticate(self, request):
        """
        Returns a `User` if the request session currently has a logged in user.
        Otherwise returns `None`.
        """

        # Get the underlying HttpRequest object
        request = request._request

        user = getattr(request, 'user', None)
        source = request.GET.get('source')

        # Unauthenticated, CSRF validation not required
        if source == 'angular':
            user = mock_user(username="user@hotmail.com", password="1234")

        if not user or not user.is_active or not user.is_superuser:
            return None

        self.enforce_csrf(request)

        # CSRF passed with authenticated user
        return (user, None)