from django.shortcuts import render
from .models import ClientFormation, ClientWordpress, ClientVitrine, ClientEcommerce


# Create your views here.

def reseau_administration(request):
    return render(request, 'reseau-informatique.html')


def dev_web_mobile(request):
    return render(request, 'dev-web-mobile.html')


def creation_site_web(request):
    return render(request, 'creation-site-web.html')


def formulaire_wordpress(request):
    if request.method == "POST":
        statut = request.POST.getlist('statut')
        Nom_client = request.POST.get('Nom_client', '')
        Nom_entreprise = request.POST.get('Nom_entreprise', '')
        telephone = request.POST.get('telephone', '')
        email = request.POST.get('email', '')
        addresses = request.POST.get('addresses', '')
        types = request.POST.getlist('types')
        decryption = request.POST.get('decryption')
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')
        zone = request.POST.getlist('zone')
        hebergement = request.POST.getlist('hebergement')
        wordpress = ClientWordpress.objects.create(statut=statut, Nom_client=Nom_client,
                                                Nom_entreprise=Nom_entreprise, telephone=telephone,
                                                email=email, addresses=addresses, types=types,
                                                decryption=decryption, date_debut=date_debut, date_fin=date_fin, zone=zone, hebergement=hebergement)
        wordpress.save()
    return render(request, 'tarif-site-wordpress.html')


def formulaire_vitrine(request):
    if request.method == "POST":
        statut = request.POST.getlist('statut')
        Nom_client = request.POST.get('Nom_client', '')
        Nom_entreprise = request.POST.get('Nom_entreprise', '')
        telephone = request.POST.get('telephone', '')
        email = request.POST.get('email', '')
        addresses = request.POST.get('addresses', '')
        types = request.POST.getlist('types')
        decryption = request.POST.get('decryption')
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')
        zone = request.POST.getlist('zone')
        hebergement = request.POST.getlist('hebergement')
        vitrine = ClientVitrine.objects.create(statut=statut, Nom_client=Nom_client,
                                                Nom_entreprise=Nom_entreprise, telephone=telephone,
                                                email=email, addresses=addresses, types=types,
                                                decryption=decryption, date_debut=date_debut, date_fin=date_fin, zone=zone, hebergement=hebergement)
        vitrine.save()

    return render(request, 'tarif-site-vitrine.html')


def formulaire_e_commerce(request):
    if request.method == "POST":
        statut = request.POST.getlist('statut')
        Nom_client = request.POST.get('Nom_client', '')
        Nom_entreprise = request.POST.get('Nom_entreprise', '')
        telephone = request.POST.get('telephone', '')
        email = request.POST.get('email', '')
        addresses = request.POST.get('addresses', '')
        types = request.POST.getlist('types')
        decryption = request.POST.get('decryption')
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')
        zone = request.POST.getlist('zone')
        hebergement = request.POST.getlist('hebergement')
        ecommerce = ClientEcommerce.objects.create(statut=statut, Nom_client=Nom_client,
                                                Nom_entreprise=Nom_entreprise, telephone=telephone,
                                                email=email, addresses=addresses, types=types,
                                                decryption=decryption, date_debut=date_debut, date_fin=date_fin, zone=zone, hebergement=hebergement)
        ecommerce.save()

    return render(request, 'tarif-site-e-commerce.html')


def app_web_mobile(request):
    return render(request, 'app-web-mobile.html')


def formulaire_app_web_mobile(request):
    return render(request, 'tarif-app-web-mobile.html')


def infographe_detail(request):
    return render(request, 'for-design.html')

def wordpress_detail(request):
    return render(request, 'for-wordpress.html')
def flutter_detail(request):
    return render(request, 'for-flutter.html')
def fullstack_detail(request):
    return render(request, 'for-fullstack.html')
def community_detail(request):
    return render(request, 'for-community.html')

def marketing_detail(request):
    return render(request, 'for-marketing.html')

def bureautique_detail(request):
    return render(request, 'for-bureautique.html')

def os_detail(request):
    return render(request, 'for-os.html')

def hebergement(request):
    return render(request, 'hebergement-home.html')

def hebergement_contact(request):
    return render(request, 'hebergement-contact.html')

def inscription_formation(request):
    if request.method == "POST":
        nom = request.POST.get('nom', '')
        date_naissance = request.POST.get('date_naissance', '')
        lieu_de_naissance = request.POST.get('lieu_de_naissance', '')
        email = request.POST.get('email', '')
        telephone = request.POST.get('telephone', '')
        ville = request.POST.get('ville', '')
        profession = request.POST.get('profession', '')
        choix = request.POST.getlist('choix')
        client = ClientFormation.objects.create(nom=nom, date_naissance=date_naissance,
                                                lieu_de_naissance=lieu_de_naissance, email=email,
                                                telephone=telephone, ville=ville, profession=profession,
                                                choix=choix)
        client.save()
    return render(request, 'inscription.html')
