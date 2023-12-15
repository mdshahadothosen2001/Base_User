import random
from django.core.mail import send_mail
from django.conf import settings
from .models import OTPModel


def send_otp_to_email(email):
    """Used to generate otp and send through email"""

    otp = random.randint(1000, 9999)

    try:
        subject = "Your OTP for registration"
        message = f"Your OTP is: {otp}"
        from_email = settings.EMAIL_HOST
        if settings.EMAIL_HOST_USER:
            send_mail(subject, message, from_email, [email])
        print(f"{otp} OTP successfully sent to {email}")

        return otp

    except Exception as e:
        print("Error sending OTP :", e)


def otp_send(email):
    """Used to call send otp function and save otp to the otp model"""

    otp = send_otp_to_email(email)

    try:
        otp_instance = OTPModel.objects.get(email=email)
        otp_instance.otp = otp
        otp_instance.save()

    except OTPModel.DoesNotExist:
        otp_instance = OTPModel.objects.create(email=email, otp=otp)