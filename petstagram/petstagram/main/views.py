from django.shortcuts import render


def show_home(request):
    context = {
        'hide_additional_nav_items': True,
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    return render(request, 'dashboard.html')


def show_profile(request):
    return render(request, 'profile_details.html')


def show_pet_photo_details(request, pk):
    return render(request, 'photo_details.html')