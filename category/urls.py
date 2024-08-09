from django.urls import path
from .views import create_category,get_category_by_id,get_all_categories,update_category,delete_category,get_categories_by_status


urlpatterns = [
    path('create_category/', create_category, name='create_category'),
    path('get_category_by_id/<uuid:id>/', get_category_by_id, name='get_category_by_id'),
    path('get_all_categories/', get_all_categories, name='get_all_categories'),
    path('update_category/<uuid:id>/', update_category, name='update_category'),
    path('delete_category/<uuid:id>/', delete_category, name='delete_category'),
    path('get_categories_by_status/', get_categories_by_status, name='get_categories_by_status'),

]
