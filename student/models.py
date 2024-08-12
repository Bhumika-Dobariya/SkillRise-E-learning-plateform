from django.db import models
import uuid
from django.utils import timezone

class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('User.User', on_delete=models.CASCADE, related_name='students')
    email = models.EmailField(unique=True, blank=False)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    education = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now) 
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.user:
            self.email = self.user.email
            self.name = self.user.name
        super(Student, self).save(*args, **kwargs)