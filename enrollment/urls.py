from django.urls import path
from . import views 

urlpatterns = [
    path('create_enrollment/', views.create_enrollment, name='create_enrollment'),
    path('get_enrollment_by_id/', views.get_enrollment_by_id, name='get_enrollment_by_id'),
    path('get_all_enrollments/', views.get_all_enrollments, name='get_all_enrollments'),
    path('update_enrollment/', views.update_enrollment, name='update_enrollment'),
    path('delete_enrollment/', views.delete_enrollment, name='delete_enrollment'),
    path('get_enrollments_by_student/', views.get_enrollments_by_student, name='get_enrollments_by_student'),
    path('get_enrollments_by_course/', views.get_enrollments_by_course, name='get_enrollments_by_course'),
    path('issue_certificate/', views.issue_certificate, name='issue_certificate'),
    path('get_enrollments_by_completion_date/', views.get_enrollments_by_completion_date, name='get_enrollments_by_completion_date'),
]