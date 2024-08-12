from django.urls import path
from . import views

urlpatterns = [
    path('get_all_students/', views.get_all_students, name='get_all_students'),
    path('get_student_by_id/', views.get_student_by_id, name='get_student_by_id'),
    path('create_student/', views.create_student, name='create_student'),
    path('update_student/', views.update_student, name='update_student'),
    path('delete_student/', views.delete_student, name='delete_student'),
    path('list_students_with_filters/', views.list_students_with_filters, name='list_students_with_filters'),
    path('students_by_gender/',views.get_students_by_gender, name='get_students_by_gender'),
]
