from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect


def index(request):
    return render(request, 'landing.html')


def about(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contactus.html')


def logout(request):
    # return logout(request)
    auth_logout(request)
    return redirect('/')


# @api_view(['POST'])
# def api_contactus_submit(request, contact_us)
