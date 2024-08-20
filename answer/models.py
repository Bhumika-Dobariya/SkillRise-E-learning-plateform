from django.db import models
import uuid

class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey('question.Question', on_delete=models.CASCADE)
    answer_text = models.TextField()
    is_correct = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_text
