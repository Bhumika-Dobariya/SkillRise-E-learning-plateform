from django.urls import path
from .views import (
    create_answer,
    get_answer_by_id,
    get_all_answers,
    update_answer,
    delete_answer,
    get_answers_by_question,
    get_answers_by_correctness
)

urlpatterns = [
    path('create_answer/', create_answer, name='create_answer'),
    path('get_answer_by_id/', get_answer_by_id, name='get_answer_by_id'),
    path('get_all_answers/', get_all_answers, name='get_all_answers'),
    path('update_answer/', update_answer, name='update_answer'),
    path('delete_answer/', delete_answer, name='delete_answer'),
    path('get_answers_by_question/', get_answers_by_question, name='get_answers_by_question'),
    path('get_answers_by_correctness/', get_answers_by_correctness, name='get_answers_by_correctness'),  
]
