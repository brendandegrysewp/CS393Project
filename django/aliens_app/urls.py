from django.urls import path
from . import views
from .models import User

urlpatterns = [
    path("", views.index, name="index"),
    path("cadmin", views.administer, name="cadmin"),
    path("cadmin/<str:username>", views.del_user, name="delete"),
    path("sightings/<int:startIndex>", views.sightings, name="sightings"),
    path("sightings/item/<int:sightingId>", views.view_sighting, name="view_sighting"),
    # path("sightings/item/<int:sightingId>/add_comment", views.add_comment, name="add_comment"),
    # path("sightings/item/<int:sightingId>/add_gov", views.add_gov, name="add_gov"),
    path("reports/", views.reports, name="reports"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("login/register/", views.register, name="register"),
]