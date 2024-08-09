from django.db import models
from django.utils import timezone

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    module = models.ForeignKey('Module.Module', on_delete=models.CASCADE, related_name='lessons')
    chapter = models.IntegerField() 
    duration = models.DurationField()  
    video_url = models.URLField(blank=True, null=True)  
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['chapter']  

    def __str__(self):
        return self.title