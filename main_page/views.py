import datetime

from django.shortcuts import render, HttpResponse
from .models import Category, Dishes, AboutUs, BlockOfInformation, Events, PhotoToGallery, CrewMember,\
    CustomerFeedback, HeroSection
# Create your views here.


def main_page(request):
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


    }
    return render(request, 'main_page.html', context=data)
