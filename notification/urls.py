from django.urls import path
from . import views

urlpatterns = [
    
    path('send_notification/', views.send_notification, name='send_notification'),
    path('notifications/', views.get_notification_by_id, name='get_notification_by_id'),
    path('notifications/all/', views.get_all_notifications, name='get_all_notifications'),
    path('notifications/update/', views.update_notification, name='update_notification'),
    path('notifications/delete/', views.delete_notification, name='delete_notification'),
    path('notifications/mark_as_read/', views.mark_notification_as_read, name='mark_notification_as_read'),
    path('send_sms/', views.send_notification, name='send_notification'),  # Example URL pattern for sending SMS
]

