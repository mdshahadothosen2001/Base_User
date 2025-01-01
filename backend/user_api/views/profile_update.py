from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user_api.serializers.profile_update import UpdateProfileSerializer
from utils.utils import tokenValidation
from user.models import UserAccount


class UserProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        payload = tokenValidation(request)
        email = payload.get("email")

        if email:
            instance = UserAccount.objects.get(email=email)
            serializer = UpdateProfileSerializer(
                instance, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "success": True,
                        "message": "Completed process! your profile has updated",
                    }
                )

        return Response(
            {
                "success": False,
                "message": "Incompleted process! Please try with valid data",
            }
        )
