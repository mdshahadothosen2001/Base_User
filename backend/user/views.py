from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from django.utils import timezone

from .serializers import UserRegistrationSerializer
from utils.utils import tokenValidation
from utils.utils import recovery_key
from user.models import UserAccount
from otp.otp_send import otp_send
from otp.models import OTPModel


@api_view(["GET"])
@permission_classes([AllowAny])
def getRoutes(request):
    "Used for show token api path"

    routes = [
        "          Here All APIs:        ",
        "/user/register/",
        "/user/activate/",
    
        "/user/token/",
        "/user/token/refresh/",

        "/user/home/",
        
        "/user/reset/",
        "/user/forgotten/",
        "/user/profile-update/",

        "/otp/resend/",
    ]

    return Response(routes)


class UserRegistrationView(APIView):
    """Users can register their account by email, frist_name, last_name and password."""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """Used to create user account and send otp by calling otp function"""

        email = request.data.get("email")
        phone_number = request.data.get("phone_number")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        password = request.data.get("password")

        if phone_number is None or email is None or password is None:
            raise ValidationError(
                "you can not create user without fulfill phone number and email and password fields! please double check."
            )

        Is_member = UserAccount.objects.filter(email=email).values()
        if len(Is_member) != 0:
            raise ValidationError("You are already member")
        
        user_info = {
            "phone_number": phone_number,
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


class UserActivationView(APIView):
    """User can activate account by OTP received through email."""

    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs):
        """Used to update user activate status by otp confirm"""

        email = request.data.get("email")
        otp = request.data.get("otp")

        if not email or not otp:
            raise ValidationError("Please provide both email and OTP.")

        otp_obj = get_object_or_404(OTPModel, email=email, otp=otp)

        now_date = datetime.now().date()
        now_time = datetime.now().time().strftime("%H:%M:%S")

        otp_obj_date = otp_obj.created_at.date()
        validation_time = timezone.localtime(otp_obj.created_at) + timedelta(minutes=40)
        validation_time = validation_time.time().strftime("%H:%M:%S")

        if now_date != otp_obj_date:
            otp_obj.delete()

            return Response("Timeout!, OTP has expired.")

        if now_time >= validation_time:
            otp_obj.delete()

            return Response("Timeout!, OTP has expired.")

        user = UserAccount.objects.get(email=email)
        user.is_active = True
        user.save()
        otp_obj.delete()

        return Response("Your account has been activated!")


class UserPasswordResetView(APIView):
    """User can change thier password by token with new password"""

    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        """This method used to recreate user password when user logined"""

        new_password = request.data.get("new_password")

        if not new_password:
            raise ValidationError("new_password required")

        payload = tokenValidation(request)
        email = payload.get("email")

        if email:
            user = UserAccount.objects.get(email=email)
            user.set_password(new_password)
            user.save()

            return Response({"message": "successfully changed password"})

        else:
            return Response("Email not found!")


class ForgottenPasswordResetView(APIView):
    """User can recreate password by their phone number and email when user forgotten their password"""

    permission_classes = [AllowAny]

    def patch(self, request):
        """This method used to generate temporary password"""

        phone_number = request.data.get("phone_number")
        email = request.data.get("email")

        if email and phone_number:
            recovery_password = recovery_key(email)
            user = get_object_or_404(
                UserAccount, email=email, phone_number=phone_number
            )
            user.set_password(recovery_password)
            user.save()

            return Response("successfully done!")

        raise ValidationError("Required phone_number and email")


class UpdateProfileView(APIView):
    """User can update their profile information"""

    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):

        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")

        payload = tokenValidation(request)
        email = payload.get("email")

        if email:
            user = UserAccount.objects.get(email=email)
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            user.save()

            return Response({"message": "successfully update your profile"})
