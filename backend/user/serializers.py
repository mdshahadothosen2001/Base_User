from rest_framework import serializers

from .models import UserAccount


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserAccount
        fields = ["id", "phone_number", "email", "password"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user


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
        ]
