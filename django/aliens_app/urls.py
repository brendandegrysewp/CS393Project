from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sightings/<int:startIndex>", views.sightings, name="sightings"),
    path("sightings/item/<int:sightingId>", views.view_sighting, name="view_sighting"),
    # path("sightings/item/<int:sightingId>/add_comment", views.add_comment, name="add_comment"),
    # path("sightings/item/<int:sightingId>/add_gov", views.add_gov, name="add_gov"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("login/register/", views.register, name="register"),
]