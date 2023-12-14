from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from utils.models import TimeStamp
from utils.utils import PHONE_REGEX


class UserAccountManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if phone_number is None or password is None:
            raise ValueError("Phone Number & Password is required")

        user = self.model(
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin, TimeStamp):
    phone_number = models.CharField(
        validators=[PHONE_REGEX], max_length=11, unique=True
    )
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    class Gender(models.TextChoices):
        MALE = "MALE", "male"
        FEMALE = "FEMALE", "female"
        OTHERS = "OTHERS", "others"

    gender = models.CharField(
        max_length=10, choices=Gender.choices, null=True, blank=True
    )
    date_of_birth = models.DateField(null=True, blank=True)
    class MaritalStatus(models.TextChoices):
        SINGLE = "SINGLE", "single"
        MARRIED = "MARRIED", "married"
        OTHERS = "OTHERS", "others"

    marital_status = models.CharField(
        max_length=10, choices=MaritalStatus.choices, null=True, blank=True
    )
    nationality = models.CharField(max_length=255, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"

    objects = UserAccountManager()

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "UserAccount"
        verbose_name_plural = "UserAccounts"
        db_table = "user_account"
