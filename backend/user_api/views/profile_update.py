from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.profile_update import UpdateProfileSerializer
from utils.utils import tokenValidation
from user.models import UserAccount


class UserProfileUpdateView(APIView):
    """User can update their profile information"""

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
                return Response("successfully updated your profile")
        return Response("Incomplete updation! Please try with valid data")
