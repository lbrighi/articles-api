from django.contrib.auth.models import Group
from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "name",
            "groups",
            "password"
        ]
        read_only_fields = ('password',)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', [])
        user = User.objects.create(**validated_data)

        if password:
            user.set_password(password)

        user.save()

        for group in groups:
            user.groups.add(group)

        return user


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
