from django.db import models
from django.contrib.auth.models import User
import uuid



class StudentScore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='scores')
    quiz = models.ForeignKey('quize.Quiz', on_delete=models.CASCADE, related_name='scores')  
    obtained_marks = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student.username} - {self.quiz.title} - {self.obtained_marks}/{self.total_marks}"
    
class StudentAnswer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey('question.Question', on_delete=models.CASCADE, related_name='answers')  
    answer = models.TextField()
    obtained_marks = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student.username} - {self.question.question_text} - Marks: {self.obtained_marks}"
