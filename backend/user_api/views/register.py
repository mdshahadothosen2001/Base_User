from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Q

from ..serializers.register import UserRegistrationSerializer
from user.models import UserAccount
from otp.otp_send import generate_otp_and_otp_send_to_email


class UserRegistrationView(APIView):
    """Users can register their account by email, frist_name, last_name and password."""

    permission_classes = [AllowAny]

    def validate_parameter(self, phone_number, email, password):
        if phone_number and email and password:
            return True
        else:
            return False

    def have_account(self, phone_number, email):
        #    check this phone_number exists or email using complex query with OR operation.
        is_member = UserAccount.objects.filter(
            Q(phone_number=phone_number) | Q(email=email)
        ).exists()
        return is_member

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        email = request.data.get("email")
        password = request.data.get("password")

        if self.validate_parameter(phone_number, email, password) is True:
            if self.have_account(phone_number, email) is True:
                return Response("You have already account at SeeHouse")
            user_data = {
                "phone_number": phone_number,
                "email": email,
                "password": password,
            }

            serializer = UserRegistrationSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
                generate_otp_and_otp_send_to_email(email)

                return Response("Completed your registration process!")

        return Response("Incompleted registration! Please provide valid data")
