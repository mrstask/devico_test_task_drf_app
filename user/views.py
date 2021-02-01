from django.contrib.auth.models import User
from rest_framework import generics, mixins

from user.serializers import UserListSerializer, UserDetailSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = []


class UserDetail(mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
    """
    Retrieve, update a snippet instance.
    """
    queryset = User.objects.all().select_related('extendeduser')
    serializer_class = UserDetailSerializer
    permission_classes = []


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

