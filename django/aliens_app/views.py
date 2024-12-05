from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Governmentemployee, Sighting
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.contrib import messages

# Create your views here.

def index(request):
    context = {"all_employees": Governmentemployee.objects.all()}
    return render(request, "aliens_app/main.html", context)

@permission_required(["aliens.isAlien"], login_url='aliens_app/login.html')
def sightings(request):
    context = {"all_sightings": Sighting.objects.all()[:20]}
    return render(request, "aliens_app/sightings.html", context)

def login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is not None:
            auth_login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "aliens_app/login.html")

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)

    return redirect("index")