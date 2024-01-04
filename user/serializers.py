from django.contrib.auth.models import Group
from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "name",
            "groups"
        ]


class SmallUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "name"
        ]


class GroupSerializer(serializers.ModelSerializer):
    users = SmallUserSerializer(many=True, read_only=True, source='user_set')

    class Meta:
        model = Group
        fields = [
            "id",
            "name",
            "users"
        ]


class SmallGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            "id"
        ]
