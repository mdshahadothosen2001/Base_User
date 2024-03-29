from rest_framework import serializers

from user.models import UserAccount


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            "email",
            "first_name",
            "last_name",
            "gender",
            "marital_status",
            "nationality",
            "occupation",
        ]
