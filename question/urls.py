from django.urls import path
from .views import (
    create_question,
    get_question_by_id,
    get_all_questions,
    update_question,
    delete_question,
    get_questions_by_quiz,
    get_questions_by_type,
)

urlpatterns = [
    path('create_question/', create_question, name='create_question'),
    path('get_question_by_id/', get_question_by_id, name='get_question_by_id'),
    path('get_all_questions/', get_all_questions, name='get_all_questions'),
    path('update_question/', update_question, name='update_question'),
    path('delete_question/', delete_question, name='delete_question'),
    path('get_questions_by_quiz/', get_questions_by_quiz, name='get_questions_by_quiz'),
    path('get_questions_by_type/', get_questions_by_type, name='get_questions_by_type'),
]
