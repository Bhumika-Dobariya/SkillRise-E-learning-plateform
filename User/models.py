from django.db import models
import uuid
from django.utils import timezone


class User(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Student', 'Student'),
        ('Instructor', 'Instructor'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Student')
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)






class OTP(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_email = models.EmailField(max_length=254)
    otp = models.CharField(max_length=6)
    expiration_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
   
   
class BlacklistedToken(models.Model):
    token = models.TextField(unique=True)
    blacklisted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.token