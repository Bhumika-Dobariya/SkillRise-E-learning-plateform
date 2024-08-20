from django.db import models
import uuid

class Subscription(models.Model):
    SUBSCRIPTION_TYPES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
        ('lifetime', 'Lifetime'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course.Course', on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=10, choices=SUBSCRIPTION_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.student.name} - {self.course.name} ({self.subscription_type})"

