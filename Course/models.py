import uuid
from django.db import models
from django.utils import timezone


class StudentCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='student_courses')
    student = models.ForeignKey('User.User', on_delete=models.CASCADE, related_name='student_courses')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"




class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='courses')  
    instructor = models.ForeignKey('instructor.Instructor', on_delete=models.CASCADE, related_name='courses')
    student = models.ForeignKey('User.User', on_delete=models.CASCADE, related_name='courses', blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField() 
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    level = models.CharField(max_length=50)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    language = models.CharField(max_length=50) 
    is_published = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True) 
    is_active = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name