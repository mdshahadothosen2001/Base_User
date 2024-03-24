from django.db import models
from utils.models import TimeStamp


class OTPModel(TimeStamp):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "OTP"
        verbose_name_plural = "OTPs"
        db_table = "otp"
