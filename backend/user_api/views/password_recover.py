from django.shortcuts import get_object_or_404

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.utils import recovery_key
from user.models import UserAccount


class UserPasswordRecoverView(APIView):
    """This class allow to User can recover password by their phone number and email when user forgotten their password"""

    permission_classes = [AllowAny]

    def patch(self, request):
        phone_number = request.data.get("phone_number")
        email = request.data.get("email")

        if email and phone_number:
            recovery_password = recovery_key(email)
            user = get_object_or_404(
                UserAccount, email=email, phone_number=phone_number
            )
            user.set_password(recovery_password)
            user.save()
            return Response(
                {
                    "success": True,
                    "message": "Completed process! Your password has recovered and send to your email inbox",
                }
            )

        return Response(
            {
                "success": False,
                "message": "Incompleted process! please try with valid phone_number and email",
            }
        )
