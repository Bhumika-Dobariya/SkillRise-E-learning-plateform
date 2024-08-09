from django.db import models
import uuid


class User(models.Model):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin'),
    )

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default='student')
    email = models.EmailField(unique=True, blank=False)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    education = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




class OTP(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_email = models.EmailField(max_length=254)
    otp = models.CharField(max_length=6)
    expiration_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
   