from django.core.cache import cache
from django.shortcuts import get_object_or_404

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import UserAccount


class UserActivationView(APIView):
    permission_classes = [AllowAny]

    def patch(self, request):
        email = request.data.get("email")
        requested_otp = request.data.get("otp")
        user = get_object_or_404(UserAccount, email=email)

        if email and requested_otp:
            db_previous_otp = cache.get(email)
            if not db_previous_otp and user.is_active == False:
                return Response(
                    {"success": False, "message": "Timeout!, OTP has expired."}
                )

            if db_previous_otp == requested_otp:
                user.is_active = True
                user.save()
                cache.delete(email)
                return Response(
                    {"success": True, "message": "Your account has been activated!"}
                )

        return Response(
            {
                "success": False,
                "message": "Please provide valid data both email and OTP.",
            }
        )
