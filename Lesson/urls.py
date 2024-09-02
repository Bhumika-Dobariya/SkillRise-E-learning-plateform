from django.urls import path
from . import views

urlpatterns = [

    path('create_lesson/', views.create_lesson, name='create_lesson'),
    path('get_lesson_by_id/', views.get_lesson_by_id, name='get_lesson_by_id'),
    path('get_all_lessons/', views.get_all_lessons, name='get_all_lessons'),
    path('update_lesson/', views.update_lesson, name='update_lesson'),
    path('delete_lesson/', views.delete_lesson, name='delete_lesson'),
    path('get_lessons_by_module/', views.get_lessons_by_module, name='get_lessons_by_module'),
    path('get_lessons_by_chapter/', views.get_lessons_by_chapter, name='get_lessons_by_chapter'),
    path('get_active_lessons/', views.get_active_lessons, name='get_active_lessons'),
    path('get_lessons_by_duration/', views.get_lessons_by_duration, name='get_lessons_by_duration'),
    path('get_lessons_by_date_range/', views.get_lessons_by_date_range, name='get_lessons_by_date_range'),
       
]