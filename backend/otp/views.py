from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from user.models import UserAccount
from otp.otp_send import generate_otp_and_otp_send_to_email


class ResendOTPView(APIView):
    """User can resend OTP after timeout of previous OTP"""

    permission_classes = [AllowAny]

    def validate_parameter(self, email):
        if email:
            return True
        else:
            return False

    def post(self, request, *args, **kwargs):

        email = request.data.get("email")

        if self.validate_parameter(email) is True:
            is_member = UserAccount.objects.filter(
                email=email, is_active=False
            ).exists()
            if is_member is True:
                generate_otp_and_otp_send_to_email(email)
                return Response("OTP send to your inbox")
        return Response("Please try with valid email")
