from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.utils import timezone


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """This class is a custom serializer for obtaining authentication tokens"""

    @classmethod
    def get_token(cls, user):
        """Used to add additional data to the token response"""

        token = super().get_token(user)
        token["email"] = user.email
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["current_datetime"] = timezone.now().isoformat()
        token["is_active"] = user.is_active

        return token
