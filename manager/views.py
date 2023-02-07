from django.shortcuts import render, redirect
from main_page.models import UserReservation, ContactUs
# Create your views here.


def reservation_list(request):
    lst = UserReservation.objects.filter(is_processed=False)
    return render(request, 'reservations_list.html', context={
        'lst': lst
    })


def update_reservation(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservations_list')


def contact_list(request):
    all_contacts = ContactUs.objects.filter(is_processed=False)
    return render(request, 'contact_list.html', context={
        'all_contacts': all_contacts
    })

def update_contact(request, pk):
    ContactUs.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:contact_list')