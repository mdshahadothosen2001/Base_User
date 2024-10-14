import random
from django.core.mail import send_mail
from django.conf import settings

from .models import OTPModel


def generate_otp_and_otp_send_to_email(email):
    """Used to generate otp and email sending included subject and meesage with otp"""

    otp = random.randint(1000, 9999)
    subject = "Your OTP for account activation"
    message = f"Your OTP is: {otp}"
    from_email = settings.EMAIL_HOST
    if settings.EMAIL_HOST_USER and settings.EMAIL_HOST_PASSWORD:
        send_mail(subject, message, from_email, [email])
    otp_instance_save(email, otp)
    return otp


def otp_instance_save(email, otp):
    """Used to save otp instance to the otp model with user email as key"""

    otp_instance, created = OTPModel.objects.get_or_create(email=email)
    otp_instance.otp = otp
    otp_instance.save()
