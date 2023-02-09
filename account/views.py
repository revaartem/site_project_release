from django.shortcuts import render
from .forms import UserRegistration
from main_page.models import InformationInContactUs, Footer


def registration_view(request):
    form = UserRegistration(request.POST or None)
    information_in_contact_us = InformationInContactUs.objects.get()
    footer = Footer.objects.get()
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return render(request, 'registration_done.html', context={'user': new_user})

    data = {
        'form': form,
        'information_in_contact_us': information_in_contact_us,
        'footer': footer,

    }

    return render(request, 'registration.html', context=data)