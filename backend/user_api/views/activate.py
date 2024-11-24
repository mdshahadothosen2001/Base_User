from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.cache import cache
from django.shortcuts import get_object_or_404

from user.models import UserAccount


class UserActivationView(APIView):
    """User can activate account by OTP received through email."""

    permission_classes = [AllowAny]

    def validate_parameter(self, email, otp):
        if email and otp:
            return True
        else:
            return False

    def patch(self, request, *args, **kwargs):
        """Used to update user activate status by otp confirm"""

        email = request.data.get("email")
        requested_otp = request.data.get("otp")
        user = get_object_or_404(UserAccount, email=email)

        if self.validate_parameter(email, requested_otp) is True:
            db_previous_otp = cache.get(email)
            print(db_previous_otp)
            if not db_previous_otp and user.is_active == False:
                return Response("Timeout!, OTP has expired.")

            if db_previous_otp == requested_otp:
                user.is_active = True
                user.save()
                cache.delete(email)
                return Response("Your account has been activated!")

        return Response("Please provide valid data both email and OTP.")
