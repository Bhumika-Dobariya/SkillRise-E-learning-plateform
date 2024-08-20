from django.db import models
import uuid
from quize.models import Quiz

    

class Question(models.Model):
    QUESTION_TYPES = [
        ('SA', 'Short Answer'),
        ('MCQ', 'Multiple Choice Question'),
        ('TF', 'True/False'),
        ('FIB', 'Fill in the Blanks'),
        ('ESSAY', 'Essay'),
        ('MATCH', 'Matching'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.CharField(max_length=6, choices=QUESTION_TYPES)  
    marks = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text

