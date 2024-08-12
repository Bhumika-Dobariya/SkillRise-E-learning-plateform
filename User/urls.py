from django.urls import path
from .views import (
    admin_only_view,
    create_user,
    generate_otp,
    verify_otp,
    login_or_register,
    get_user_by_id,
    get_user_by_token,
    get_all_user,
    update_user,
    update_user_by_token,
    user_delete,
    user_delete_by_token,
    forget_password,
    reset_password_by_token,
    logout,
    instructor_only_view,
    student_only_view
)

urlpatterns = [
    path('admin-only/', admin_only_view, name='admin_only_view'),

    # User management
    path('create_user/', create_user, name='create_user'),
    path('get_user_by_id/<uuid:id>/', get_user_by_id, name='get_user_by_id'), 
    path('get_user_by_token/', get_user_by_token, name='get_user_by_token'),
    path('get_all_user/', get_all_user, name='get_all_users'),
    path('update_user/<uuid:id>/', update_user, name='update_user'),  
    path('update_user_by_token/', update_user_by_token, name='update_user_by_token'),
    path('user_delete/<uuid:id>/', user_delete, name='delete_user'),  
    path('user_delete_by_token/', user_delete_by_token, name='delete_user_by_token'),

    # OTP Management
    path('generate_otp/', generate_otp, name='generate_otp'),
    path('verify_otp/', verify_otp, name='verify_otp'),

    # Password management
    path('forget_password/', forget_password, name='forget_password'),
    path('reset_password_by_token/', reset_password_by_token, name='reset_password_by_token'),

    # User registration and login
    path('login_or_register/', login_or_register, name='login_or_register'),

    # Logout
    path('logout/', logout, name='logout'),
  
    path('admin_only_view/', admin_only_view, name='admin_only_view'),
    path('instructor_only_view/', instructor_only_view, name='instructor_only_view'),
    path('student_only_view/', student_only_view, name='student_only_view'),

]