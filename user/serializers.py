from django.contrib.auth.models import User
from rest_framework import serializers

from user.models import ExtendedUser


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (('email',
                   'username',
                   'password',
                   'id',
                   ))

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    last_visit = serializers.DateTimeField(source='extendeduser.last_visit')

    class Meta:
        model = User
        fields = ('username',
                  'last_login',
                  'last_visit'
                  )
