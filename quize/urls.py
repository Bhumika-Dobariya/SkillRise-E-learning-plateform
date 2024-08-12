from django.urls import path
from .views import create_quiz, get_quiz_by_id, get_all_quizzes, update_quiz, delete_quiz,get_quizzes_by_module,get_quizzes_by_instructor

urlpatterns = [
    path('create_quiz/', create_quiz, name='create_quiz'),
    path('get_quiz_by_id/', get_quiz_by_id, name='get_quiz_by_id'),
    path('get_all_quizzes/', get_all_quizzes, name='get_all_quizzes'),
    path('update_quiz/', update_quiz, name='update_quiz'),
    path('delete_quiz/', delete_quiz, name='delete_quiz'),
    path('get_quizzes_by_module/', get_quizzes_by_module, name='get_quizzes_by_module'),
    path('get_quizzes_by_instructor/', get_quizzes_by_instructor, name='get_quizzes_by_instructor'),
]