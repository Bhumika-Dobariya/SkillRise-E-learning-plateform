
from django.urls import path
from .views import create_course,get_course_by_id,get_all_courses,update_course,delete_course,add_student_to_course,get_students_by_course,get_student_course_by_id,get_all_student_courses,update_student_course,delete_student_course,get_courses_by_category,get_courses_by_instructor


urlpatterns = [
    
    path('add_student_to_course/', add_student_to_course, name='add_student_to_course'),
    path('get_student_course_by_id/', get_student_course_by_id, name='get_student_course_by_id'),
    path('get_students_by_course/', get_students_by_course, name='get_students_by_course'),
    path('get_all_student_courses/', get_all_student_courses, name='get_all_student_courses'),
    path('update_student_course/', update_student_course, name='update_student_course'),
    path('delete_student_course/', delete_student_course, name='delete_student_course'),
    path('create_course/', create_course, name='create_course'),
    path('get_course_by_id/', get_course_by_id, name='get_course_by_id'),
    path('get_all_courses/', get_all_courses, name='get_all_courses'),
    path('update_course/', update_course, name='update_course'),
    path('delete_course/', delete_course, name='delete_course'),
    path('get_courses_by_category/', get_courses_by_category, name='get_courses_by_category'),
    path('get_courses_by_instructor/', get_courses_by_instructor, name='get_courses_by_instructor'),
   

]


