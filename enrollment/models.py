from django.db import models
from django.utils import timezone
import uuid


class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='enrollment', blank=True, null=True)
    course = models.ForeignKey('Course.Course', on_delete=models.CASCADE, related_name='enrollment') 
    enrollment_date = models.DateTimeField(default=timezone.now) 
    progress = models.FloatField(default=0.0)  
    completion_date = models.DateTimeField(null=True, blank=True)  
    is_active = models.BooleanField(default=True)  
    certificate_issued = models.BooleanField(default=False) 
    payment_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  
    payment_status = models.CharField(max_length=20, default='Pending')  
    is_paid = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.name}"