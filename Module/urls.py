from django.urls import path
from .views import create_module,get_module_by_id,get_all_modules,update_module,delete_module,get_modules_by_course,get_published_modules,get_unpublished_modules,publish_module,unpublish_module

urlpatterns = [
    path('create_module/', create_module, name='create_module'),
    path('get_module_by_id/', get_module_by_id, name='get_module_by_id'),
    path('get_all_modules/', get_all_modules, name='get_all_modules'),
    path('update_module/', update_module, name='update_module'),
    path('delete_module/', delete_module, name='delete_module'),
    path('get_modules_by_course/', get_modules_by_course, name='get_modules_by_course'),
    path('get_published_modules/', get_published_modules, name='get_published_modules'),
    path('get_unpublished_modules/', get_unpublished_modules, name='get_unpublished_modules'),
    path('publish_module/', publish_module, name='publish_module'),
    path('unpublish_module/', unpublish_module, name='unpublish_module'),
    
    
]