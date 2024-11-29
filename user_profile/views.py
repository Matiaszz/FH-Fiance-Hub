from django.shortcuts import render


def temp_view(request):
    return render(request, 'profile/profile.html')
