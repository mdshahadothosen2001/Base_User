from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from user.models import UserAccount
from utils.utils import generate_otp_and_otp_send_to_email


class ResendOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        if email:
            is_member = UserAccount.objects.filter(
                email=email, is_active=False
            ).exists()
            if is_member is True:
                otp = generate_otp_and_otp_send_to_email(email)
                return Response(
                    {"success": True, "message": "OTP send to your inbox", "data": otp}
                )

        return Response({"success": False, "message": "Please try with valid email"})
