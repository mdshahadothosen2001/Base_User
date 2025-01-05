from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.utils import tokenValidation
from user.models import UserAccount


class UserPasswordChangeView(APIView):
    """This class allow to User can change thier password by Access Token with new password"""

    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        new_password = request.data.get("new_password")

        if new_password:
            payload = tokenValidation(request)
            email = payload.get("email")
            if email:
                user = UserAccount.objects.get(email=email)
                user.set_password(new_password)
                user.save()

                return Response(
                    {
                        "success": True,
                        "message": "Completed process! password has been changed",
                    }
                )

        return Response(
            {
                "success": False,
                "message": "Incompleted process! please try with new password",
            }
        )
