from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.utils import tokenValidation
from user.models import UserAccount


class UserPasswordChangeView(APIView):
    """User can change thier password by token with new password when they are login"""

    permission_classes = [IsAuthenticated]

    def validate_parameter(self, new_password):
        if new_password:
            return True
        else:
            return False

    def patch(self, request, *args, **kwargs):
        new_password = request.data.get("new_password")

        if self.validate_parameter(new_password) is True:
            payload = tokenValidation(request)
            email = payload.get("email")
            if email:
                user = UserAccount.objects.get(email=email)
                user.set_password(new_password)
                user.save()

                return Response({"message": "successfully changed password"})

        return Response("Incompleted process! please try with new password")
