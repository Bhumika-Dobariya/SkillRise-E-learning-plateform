from django.db import models
from django.core.exceptions import ValidationError
import uuid

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipient = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='Notification', blank=True, null=True)
    message = models.TextField()
    notification_type = models.CharField(max_length=50, choices=[
        ('course_update', 'Course Update'),
        ('new_course', 'New Course'),
        ('payment', 'Payment'),
        ('reminder', 'Reminder'),
        ('general', 'General'),
    ])
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Adjust length if needed

    def clean(self):
        super().clean()
        if self.phone_number:
            if not self.phone_number.startswith('+'):
                raise ValidationError('Phone number must start with "+"')
            if len(self.phone_number) != 13:  
                raise ValidationError('Phone number must be exactly 13 characters long (including "+91").')
            if not self.phone_number[1:].isdigit():
                raise ValidationError('Phone number must contain only digits after the "+".')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Notification to {self.recipient.user.username} - {self.notification_type}'
