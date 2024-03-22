from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from utils.utils import recovery_key
from user.models import UserAccount


class UserPasswordRecoverView(APIView):
    """User can recover password by their phone number and email when user forgotten their password"""

    permission_classes = [AllowAny]

    def validate_parameter(self, email, phone_number):
        if email and phone_number:
            return True
        else:
            return False

    def patch(self, request):
        phone_number = request.data.get("phone_number")
        email = request.data.get("email")

        if self.validate_parameter(email, phone_number) is True:
            recovery_password = recovery_key(email)
            user = get_object_or_404(
                UserAccount, email=email, phone_number=phone_number
            )
            user.set_password(recovery_password)
            user.save()
            return Response("successfully recover your password!")

        return Response("Incomplete! please try with valid phone_number and email")
