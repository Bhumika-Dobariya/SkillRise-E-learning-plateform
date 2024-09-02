import uuid
from django.db import models
from django.utils import timezone

class Payment(models.Model):
    PENDING = 'P'
    COMPLETED = 'C'
    FAILED = 'F'
    
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50) 
    payment_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    transaction_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Payment {self.transaction_id} - {self.get_payment_status_display()}'
