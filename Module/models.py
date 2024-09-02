from django.db import models
import uuid

class Module(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey('Course.Course', on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    chapter = models.PositiveIntegerField()
    content = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)  
    quiz_url = models.URLField(blank=True, null=True)    
    assignment_url = models.URLField(blank=True, null=True) 
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['chapter']

    def __str__(self):
        return f'{self.title} ({self.course.name})'