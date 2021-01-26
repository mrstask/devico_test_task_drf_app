from django.contrib.auth.models import update_last_login, User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.views import TokenViewBase


class TokenAuthenticationView(TokenViewBase):
    """Implementation of ObtainAuthToken with last_login update"""
    serializer_class = serializers.TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        result = super(TokenAuthenticationView, self).post(request)
        try:
            user = User.objects.get(username=self.request.data['username'])
            update_last_login(None, user)
        except Exception as exc:
            return None
        return result