from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, "Acceuil.html")


def services (request):
    return render(request, "Services.html")


def whoWeare (request):
    return render(request, "QuiSommesNous.html")


def team (request):
    return render(request, "NotreEquipe.html")

def contact (request):
    return render(request, "Contact.html")