from django.urls import path
from .views import reservation_list, update_reservation, contact_list, update_contact, manager_page

app_name = 'manager'

urlpatterns = [
    path('reservations/', reservation_list, name='reservations_list'),
    path('reservations/update/<int:pk>', update_reservation, name='update_reserve'),
    path('contact/', contact_list, name='contact_list'),
    path('contact/update/<int:pk>', update_contact, name='update_contact'),
    path('', manager_page, name='manager_page')
]