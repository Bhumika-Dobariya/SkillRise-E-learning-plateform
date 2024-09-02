from django.db import models
import uuid
from django.utils import timezone

class Instructor(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)  
    course_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)  
    gender = models.CharField(max_length=10, blank=True, null=True) 
    date_of_joining = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
