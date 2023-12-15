from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from .serializers import UserRegistrationSerializer
from otp.otp_send import otp_send



class UserRegistrationView(APIView):
    """Users can register their account by email, frist_name, last_name and password."""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """Used to create user account and send otp by calling otp function"""

        phone_number = request.data.get("phone_number")
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        password = request.data.get("password")

        if phone_number is None or email is None:
            raise ValidationError(
                "you can not create user without fulfill phone number and email fields!"
            )

        user_info = {
            "phone_number":phone_number,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "password": password,
        }

        serializer = UserRegistrationSerializer(data=user_info)
        if serializer.is_valid():
            serializer.save()
            otp_send(email)
            
            return Response("succesfull! user is created")
