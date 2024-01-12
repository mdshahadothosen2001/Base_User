from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError

from otp.models import OTPModel
from otp.otp_send import otp_send


class ResentOTPView(APIView):
    """User can resend OTP after timeout of previous OTP"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        email = request.data.get("email")

        if email is None:
            raise ValidationError(
                "Can not send OTP without email!, must include email"
            )
        
        previous_OTP = OTPModel.objects.filter(email=email)
        if len(previous_OTP) == 0:
            otp_send(email)
            return Response("You check OTP at your terminal or email inbox")
        else:
            previous_OTP.delete()
            otp_send(email)
            return Response("You check OTP at your terminal or email inbox")
