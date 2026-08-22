from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from datetime import timedelta
from django.utils import timezone

class ExpireTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid Token')

        if token.created < timezone.now() - timedelta(minutes=1):
            token.delete()
            raise exceptions.AuthenticationFailed('Token has expired. Please login again to gain the token')
        return (token.user, token)

