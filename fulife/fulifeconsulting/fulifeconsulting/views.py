from django.http import HttpResponse
from django.shortcuts import render


#creation d´une fonction de la parametre request qui va recuperer la requete
def index(request):
    return render(request, "index.html")

#def contact(request):
 #   return render(request, "contact.html")
def contact():
    return None