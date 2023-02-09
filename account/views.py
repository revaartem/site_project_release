from django.shortcuts import render, redirect
from .forms import UserRegistration, UserLogin
from main_page.models import InformationInContactUs, Footer
from django.contrib.auth import login, authenticate, logout


def registration_view(request):
    form = UserRegistration(request.POST or None)
    information_in_contact_us = InformationInContactUs.objects.get()
    footer = Footer.objects.get()
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        data = {
            'user': new_user,
            'information_in_contact_us': information_in_contact_us,
            'footer': footer}
        return render(request, 'registration_done.html', context=data)

    data = {
        'form': form,
        'information_in_contact_us': information_in_contact_us,
        'footer': footer,
    }
    return render(request, 'registration.html', context=data)


def login_view(request):
    form = UserLogin(request.POST or None)
    next_get = request.GET.get('next')
    information_in_contact_us = InformationInContactUs.objects.get()
    footer = Footer.objects.get()

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        next_post = request.POST.get('next')
        return redirect(next_get or next_post or '/')

    data = {
        'form': form,
        'information_in_contact_us': information_in_contact_us,
        'footer': footer,
    }

    return render(request, 'login.html', context=data)


def logout_view(request):
    logout(request)
    return redirect('/')