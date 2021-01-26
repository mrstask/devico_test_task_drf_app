from user.models import ExtendedUser
from rest_framework_simplejwt import authentication

from django.utils import timezone


class AccountLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if authentication.JWTAuthentication().authenticate(request):
            request_user = authentication.JWTAuthentication().authenticate(request)[0]
            if request_user.is_authenticated:
                if ExtendedUser.objects.filter(user_id=request_user.id).exists():
                    ExtendedUser.objects.filter(user_id=request_user.id).update(last_visit=timezone.now())
                else:
                    ExtendedUser(user_id=request_user.id, last_visit=timezone.now()).save()

        response = self.get_response(request)
        return response
