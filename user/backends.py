from django.contrib.auth.backends import ModelBackend

from user.models import User


class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=email)
            except User.DoesNotExist:
                return None
        return user if user.check_password(password) else None
