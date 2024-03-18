from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from django.utils import timezone


from user.models import UserAccount
from otp.models import OTPModel


class UserActivationView(APIView):
    """User can activate account by OTP received through email."""

    permission_classes = [AllowAny]

    def validate_parameter(self, email, otp):
        if email and otp:
            return True
        else:
            return False

    def validate_otp(self, otp_obj):
        now_date = datetime.now().date()
        now_time = datetime.now().time().strftime("%H:%M:%S")

        otp_obj_date = otp_obj.created_at.date()
        validation_time = timezone.localtime(otp_obj.created_at) + timedelta(minutes=40)
        validation_time = validation_time.time().strftime("%H:%M:%S")

        if now_date != otp_obj_date or now_time >= validation_time:
            otp_obj.delete()
            return False
        return True

    def patch(self, request, *args, **kwargs):
        """Used to update user activate status by otp confirm"""

        email = request.data.get("email")
        otp = request.data.get("otp")

        if self.validate_parameter(email, otp) is True:
            otp_obj = get_object_or_404(OTPModel, email=email, otp=otp)
            if self.validate_otp(otp_obj) is True:
                user = UserAccount.objects.get(email=email)
                user.is_active = True
                user.save()
                otp_obj.delete()
                return Response("Your account has been activated!")
            return Response("Timeout!, OTP has expired.")
        return Response("Please provide valid data both email and OTP.")
