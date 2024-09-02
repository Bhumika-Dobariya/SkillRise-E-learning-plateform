from django.urls import path
from .views import (
    create_student_score, get_student_score_by_id, get_all_student_scores,
    update_student_score, delete_student_score, get_scores_by_student,
    get_scores_by_quiz, create_student_answer, get_student_answer_by_id,
    get_all_student_answers, update_student_answer, delete_student_answer,
    get_answers_by_student, get_answers_by_quiz, get_student_answers_summary
)

urlpatterns = [
    # Student Score URLs
    path('get_all_student_scores/', get_all_student_scores, name='get_all_student_scores'),
    path('get_student_score_by_id/', get_student_score_by_id, name='get_student_score_by_id'),
    path('create_student_score/', create_student_score, name='create_student_score'),
    path('update_student_score/', update_student_score, name='update_student_score'),
    path('delete_student_score/', delete_student_score, name='delete_student_score'),
    path('get_scores_by_student/', get_scores_by_student, name='get_scores_by_student'),
    path('get_scores_by_quiz/', get_scores_by_quiz, name='get_scores_by_quiz'),

    # Student Answer URLs
    path(' get_all_student_answers/', get_all_student_answers, name='get_all_student_answers'),
    path(' get_student_answer_by_id/', get_student_answer_by_id, name='get_student_answer_by_id'),
    path('create_student_answer/', create_student_answer, name='create_student_answer'),
    path('update_student_answer/', update_student_answer, name='update_student_answer'),
    path('delete_student_answe/', delete_student_answer, name='delete_student_answer'),
    path('get_answers_by_student/', get_answers_by_student, name='get_answers_by_student'),
    path('get_answers_by_quiz/', get_answers_by_quiz, name='get_answers_by_quiz'),
    path('get_student_answers_summary/', get_student_answers_summary, name='get_student_answers_summary'),
]
