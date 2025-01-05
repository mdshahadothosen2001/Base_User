from rest_framework.authentication import get_authorization_header
from django.core.cache import cache
from django.core.validators import RegexValidator
from config.JWT_SETTINGS import JWT_SETTINGS
from django.core.mail import send_mail
from django.conf import settings

import jwt
import random
import string

from config.email_host_data import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


PHONE_REGEX = RegexValidator(
    regex=r"^01[13-9]\d{8}$",
    message="Phone number must be 11 digit & this format: '01*********'",
)


def tokenValidation(request):
    """
    It takes the token from the request header, decodes it, and returns the payload
    :param request: The request object that was sent to the view
    :return: The payload of the token.
    """
    token_header = get_authorization_header(request).decode("utf-8")
    token_header_split = token_header.split(" ")
    if token_header_split[0] == "Bearer":
        token = token_header_split[1]
        payload = jwt.decode(
            jwt=token, key=JWT_SETTINGS["SIGNING_KEY"], algorithms=["HS256"]
        )
        return payload
    else:
        return None


def recovery_key(email):
    """Used to send recover password"""

    recovery_password = generate_random_string(9)

    subject = "Your recovery password"
    message = f"Your recovery password is {recovery_password}. You can login by this key then you should change your password after login."
    from_email = settings.EMAIL_HOST_USER
    if EMAIL_HOST_USER and EMAIL_HOST_PASSWORD:
        send_mail(subject, message, from_email, [from_email])

    print(message)

    return recovery_password


def generate_random_string(length):
    """Used to generate random password"""

    characters = string.ascii_letters + string.digits
    random_string = "".join(random.choice(characters) for i in range(length))

    return random_string


def data_set_to_cache(key, value, timeout):
    if key and value and timeout:
        cache.set(key, value, timeout)
        return True

    return False


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
