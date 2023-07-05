from django.shortcuts import render
from .models import Client_contact
# Create your views here.

def contact(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        detail = request.POST.get('detail')
        client = Client_contact.objects.create(nom=nom, email=email, telephone=telephone, detail=detail)
        client.save()
    return render(request, 'contact.html')
