from django.urls import path
from .views import (
    create_subscription,
    get_subscription_by_id,
    get_all_subscriptions,
    update_subscription,
    delete_subscription,
    get_subscriptions_by_student,
)

urlpatterns = [
    path('create_subscription/', create_subscription, name='create_subscription'),
    path('get_subscription_by_id/', get_subscription_by_id, name='get_subscription_by_id'),
    path('get_all_subscriptions/', get_all_subscriptions, name='get_all_subscriptions'),
    path('update_subscription/', update_subscription, name='update_subscription'),
    path('delete_subscription/', delete_subscription, name='delete_subscription'),
    path('get_subscriptions_by_student/', get_subscriptions_by_student, name='get_subscriptions_by_student'),
]
