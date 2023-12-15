from django.db import models
from utils.models import TimeStamp

class OTPModel(TimeStamp):
    """save otp and then used to active user account"""

    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)

    def __str__(self):
        """used to return email when convert object data to string"""

        return self.email
