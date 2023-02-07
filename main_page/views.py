import datetime

from django.shortcuts import render, HttpResponse, redirect
from .models import Category, Dishes, AboutUs, BlockOfInformation, Events, PhotoToGallery, CrewMember, \
    CustomerFeedback, HeroSection, ThisIsForTest, InformationInContactUs, Footer
from .forms import UserReservationForm, ContactUsForm
# Create your views here.


def main_page(request):

    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        contact_us = ContactUsForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('/')
        if contact_us.is_valid():
            contact_us.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    dishes = Dishes.objects.filter(is_visible=True)
    specials = Dishes.objects.filter(special=True)
    about_us = AboutUs.objects.get()
    blocks_with_info = BlockOfInformation.objects.all()
    events = Events.objects.filter(event_date_and_time__gt=datetime.datetime.now())
    photo_in_gallery = PhotoToGallery.objects.all()
    crew_member = CrewMember.objects.all()
    testimonials = CustomerFeedback.objects.filter(is_visible=True).all()
    hero = HeroSection.objects.all()
    reservation = UserReservationForm()
    test = ThisIsForTest.objects.get()
    contact_us = ContactUsForm()
    information_in_contact_us = InformationInContactUs.objects.get()
    footer = Footer.objects.get()

    data = {
        'categories': categories,
        'dishes': dishes,
        'specials': specials,
        'about_us': about_us,
        'blocks_with_info': blocks_with_info,
        'events': events,
        'photo_in_gallery': photo_in_gallery,
        'crew_member': crew_member,
        'testimonials': testimonials,
        'hero': hero,
        'reservation_form': reservation,
        'test': test,
        'contact_us': contact_us,
        'information_in_contact_us': information_in_contact_us,
        'footer': footer,



    }
    return render(request, 'main_page.html', context=data)
