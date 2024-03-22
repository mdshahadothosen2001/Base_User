from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from datetime import datetime


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """This class is a custom serializer for obtaining authentication tokens"""

    @classmethod
    def get_token(cls, user):
        """Used to get token and set user data"""

        token = super().get_token(user)
        token["email"] = user.email
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["current_date"] = datetime.now().strftime("%Y:%m:%d")
        current_time = datetime.now().strftime("%I:%M:%p")
        token["current_time"] = current_time

        if "AM" in current_time:
            token["day_status"] = "Day"
        else:
            token["day_status"] = "Night"

        token["location"] = "Dhaka"

        return token
