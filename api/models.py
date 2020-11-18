from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=30, blank=True)
    otp = models.CharField(max_length=30, blank=True)
    email_verification_code = models.CharField(max_length=10, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    class Meta:
        db_table = 'users'
