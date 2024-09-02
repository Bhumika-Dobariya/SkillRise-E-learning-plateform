from django.urls import path
from .views import create_instructor,get_instructor_by_id,get_all_instructors,update_instructor,delete_instructor,get_instructors_by_department

urlpatterns = [
    path('create_instructor/', create_instructor, name='create_instructor'),
    path('get_instructor_by_id/', get_instructor_by_id, name='get_instructor_by_id'),
    path('get_all_instructors/', get_all_instructors, name='get_all_instructors'),
    path('update_instructor/', update_instructor, name='update_instructor'),
    path('delete_instructor/', delete_instructor, name='delete_instructor'),
    path('get_instructors_by_department/', get_instructors_by_department, name='get_instructors_by_department'),
   
]