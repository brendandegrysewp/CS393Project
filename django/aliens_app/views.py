from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.contrib import messages
from .forms import *
import datetime
from django.contrib.contenttypes.models import ContentType

# Create your views here.

#Complex queries:
#1. Sort by believability
#2. Report most seen aliens
#3. View Aliens associated with sightings
#4. Government Notes

def index(request):
    context = {"all_employees": Governmentemployee.objects.all()}
    return render(request, "aliens_app/main.html", context)

# @permission_required(["aliens.isAlien"], login_url='aliens_app/login.html')
@login_required
def sightings(request, startIndex):
    all_sightings = Sighting.objects.raw("SELECT s.sightingId, s.date, s.comments, s.city, s.state, s.shape, s.country, s.duration, s.dateposted, s.longitude, s.latitude, SUM(c.believability) as sum, AVG(c.believability) as average FROM sighting as s LEFT JOIN comment as c ON s.sightingId = c.sightingId GROUP BY s.sightingId ORDER BY sum DESC")
    length = len(all_sightings)
    all_sightings = all_sightings[startIndex:startIndex+20]
    sform = SortForm()
    if request.method == "POST":
        form = SightingForm(request.POST)
        if form.is_valid() and "comments" in form.cleaned_data:
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
        sform = SortForm(request.POST)
        print(request.POST)
        print(sform.is_valid())
        # if sform.is_valid():
        if "highLat" in sform.cleaned_data and sform.cleaned_data["highLat"] != None:
            highLat = sform.cleaned_data["highLat"]
        else:
            highLat = 90
        if "lowLat" in sform.cleaned_data and sform.cleaned_data["lowLat"] != None:
            lowLat = sform.cleaned_data["lowLat"]
        else:
            lowLat = -90
        if "highLong" in sform.cleaned_data and sform.cleaned_data["highLong"] != None:
            highLong = sform.cleaned_data["highLong"]
        else:
            highLong = 90
        if "lowLong" in sform.cleaned_data and sform.cleaned_data["lowLong"] != None:
            lowLong = sform.cleaned_data["lowLong"]
        else:
            lowLong = -90
        if "sort" in request.POST and request.POST["sort"] != []:
            sort = request.POST["sort"]
        else:
            sort = "DESC"
        print(sform.cleaned_data)
        print(highLat,lowLat,highLong,lowLong,sort)
        all_sightings = Sighting.objects.raw(f"SELECT s.sightingId, s.date, s.comments, s.city, s.state, s.shape, s.country, s.duration, s.dateposted, s.longitude, s.latitude, SUM(c.believability) as sum, AVG(c.believability) as average FROM sighting as s LEFT JOIN comment as c ON s.sightingId = c.sightingId WHERE latitude <= %s and latitude >= %s and longitude <= %s and longitude >= %s GROUP BY s.sightingId ORDER BY sum {sort}", [highLat,lowLat,highLong,lowLong])
        length = len(all_sightings)
        all_sightings = all_sightings[startIndex:startIndex+20]
    form = SightingForm() 
    context = {"all_sightings": all_sightings, "length": length, "next": startIndex+20, "current": startIndex, "form": form, "sort": sform}
    return render(request, "aliens_app/sightings.html", context)

# @permission_required(["aliens.isAlien"], login_url='aliens_app/login.html')
@login_required
def view_sighting(request, sightingId):
    sighting = Sighting.objects.filter(sightingid=sightingId).get()
    user = get_object_or_404(User, username=request.user.username)
    user.is_staff = True
    user.save()
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
        if user.has_perm("aliens_app.isGov"):
            form = GovernmentnoteForm(request.POST)
            if form.is_valid():
                newEntry = Governmentnote(
                    sightingid = sighting,
                    # user = request.user,
                    employeeid = Governmentemployee.objects.filter(user=user).get(),
                    text = form.cleaned_data['text'],
                    date = datetime.datetime.now(),
                )
                newEntry.save()
    else:
        if user.has_perm("aliens_app.isGov"):
            form = GovernmentnoteForm()
        else:
            form = CommentForm()
    comments = Comment.objects.filter(sightingid=sightingId)
    notes = Governmentnote.objects.raw("SELECT n.noteid as noteId, name, country, position, text FROM governmentnote as n LEFT JOIN governmentemployee as e ON n.employeeId = e.employeeId WHERE n.sightingId = %s", [sightingId])
    context = {"sighting": sighting, "comments": comments, "notes": notes, "form": form}
    if user.has_perm("aliens_app.isAlien"):
        aliens = Alien.objects.raw("SELECT a.alienId as alienId, name FROM alien as a LEFT JOIN alientoexpedition as ae ON a.alienId = ae.alienId LEFT JOIN expedition as e ON ae.expeditionId = e.expeditionId WHERE sightingId = %s", [sightingId])
        # print(aliens)
        context['aliens'] = aliens
    return render(request, "aliens_app/view_sighting.html", context)

@permission_required(["aliens_app.isAlien"], login_url='aliens_app/login.html')
def reports(request):
    context = {"all_aliens": Alien.objects.raw("SELECT a.alienId, name, COUNT(ae.expeditionId) as spotted FROM alien as a LEFT JOIN alientoexpedition as ae ON a.alienId = ae.alienId LEFT JOIN expedition as e ON ae.expeditionId = e.expeditionId GROUP BY a.alienId, a.name ORDER BY spotted DESC")}
    return render(request, "aliens_app/reports.html", context)

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
            if form.cleaned_data["isGov"]:
                try:
                    permission = Permission.objects.get(codename="isGov")
                except:
                    permission = Permission.objects.create(
                        codename="isGov",
                        name="Is a government employee",
                        content_type = ContentType.objects.get_for_model(Governmentemployee)
                    )
                employee = Governmentemployee(user=user, name=user.username,country="USA",position="Top Dog")
                employee.save()
                user.user_permissions.add(permission)
            # print(form.cleaned_data['isAlien'])
            if form.cleaned_data["isAlien"]:
                try:
                    permission = Permission.objects.get(codename="isAlien")
                except:
                    permission = Permission.objects.create(
                        codename="isAlien",
                        name="Is an alien",
                        content_type = ContentType.objects.get_for_model(Alien)
                    )
                user.user_permissions.add(permission)
                user.is_staff = True
            print(user.user_permissions)
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
