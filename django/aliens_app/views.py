from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Governmentemployee, Sighting, Comment, Governmentnote
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.contrib import messages
from .forms import *
import datetime

# Create your views here.

def index(request):
    context = {"all_employees": Governmentemployee.objects.all()}
    return render(request, "aliens_app/main.html", context)

# @permission_required(["aliens.isAlien"], login_url='aliens_app/login.html')
@login_required
def sightings(request, startIndex):
    if request.method == "POST":
        form = SightingForm(request.POST)
        if form.is_valid():
            newEntry = Sighting(
                userid = request.user,
                date = form.cleaned_data['date'],
                comments = form.cleaned_data['comments'],
                city = form.cleaned_data['city'],
                state = form.cleaned_data['state'],
                shape = form.cleaned_data['shape'],
                country = form.cleaned_data['country'],
                duration = form.cleaned_data['duration'],
                dateposted = form.cleaned_data['dateposted'],
                longitude = form.cleaned_data['longitude'],
                latitude = form.cleaned_data['latitude'],
            )
            newEntry.save()
            # return render(request, "aliens_app/view_sighting.html", context)
    form = SightingForm() 
    context = {"all_sightings": Sighting.objects.all()[startIndex:startIndex+20], "next": startIndex+20, "current": startIndex, "form": form}
    return render(request, "aliens_app/sightings.html", context)

# @permission_required(["aliens.isAlien"], login_url='aliens_app/login.html')
@login_required
def view_sighting(request, sightingId):
    sighting = Sighting.objects.filter(sightingid=sightingId).get()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            newEntry = Comment(
                sightingid = sighting,
                # user = request.user,
                text = form.cleaned_data['text'],
                date = datetime.datetime.now(),
                believability = form.cleaned_data['believability'],
            )
            newEntry.save()
    form = CommentForm()
    comments = Comment.objects.filter(sightingid=sightingId)
    notes = Governmentnote.objects.filter(sightingid=sightingId)
    context = {"sighting": sighting, "comments": comments, "notes": notes, "form": form}
    return render(request, "aliens_app/view_sighting.html", context)

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

def register(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is not None:
            auth_login(request, user)
            return redirect("index")
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data["username"], form.cleaned_data["email"], form.cleaned_data["password"])
            user.save()
            return redirect("index")
        else:
            messages.error(request, "There was an issue.")
    form = RegisterForm()
    return render(request, "aliens_app/register.html", {"form": form})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)

    return redirect("index")
