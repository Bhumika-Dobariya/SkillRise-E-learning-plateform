
import uuid
from django.db import models

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

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Notification to {self.recipient.user.username} - {self.notification_type}'
