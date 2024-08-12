from django.db import models
import uuid

class Quiz(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    module = models.ForeignKey('Module.Module', on_delete=models.CASCADE, related_name='quizzes')
    instructor = models.ForeignKey('instructor.Instructor', on_delete=models.CASCADE, related_name='created_quizzes')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    total_marks = models.IntegerField()
    duration = models.DurationField()  
    passing_marks = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
