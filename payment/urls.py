from django.urls import path
from .views import (
    create_payment,
    get_payment_by_id,
    get_all_payments,
    update_payment,
    delete_payment
)

urlpatterns = [
    path('create_payment/', create_payment, name='create_payment'),
    path('get_payment_by_id/', get_payment_by_id, name='get_payment_by_id'),
    path('get_all_payments/', get_all_payments, name='get_all_payments'),
    path('update_payment/', update_payment, name='update_payment'),
    path('delete_payment/', delete_payment, name='delete_payment'),
]
