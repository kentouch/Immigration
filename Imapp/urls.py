from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='Home'),
    path("services/", views.services, name='services'),
    path("Aproposdenous/", views.whoWeare, name='QuiSommesNous'),
    path("NotreEquipe/", views.team, name='NotreEquipe'),
    path("contact", views.contact, name='contact'),
]