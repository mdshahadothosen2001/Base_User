import random
from django.core.mail import send_mail
from django.conf import settings

from utils.utils import data_set_to_cache


def generate_otp_and_otp_send_to_email(email):
    """Used to generate otp and email sending included subject and meesage with otp"""

    otp = random.randint(1000, 9999)
    subject = "Your OTP for account activation"
    message = f"Your OTP is: {otp}"
    from_email = settings.EMAIL_HOST
    if settings.EMAIL_HOST_USER and settings.EMAIL_HOST_PASSWORD:
        send_mail(subject, message, from_email, [email])

    data_set_to_cache(email, otp, 300)
    return otp
