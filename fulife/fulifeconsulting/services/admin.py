from django.contrib import admin
from .models import ClientFormation, ClientWordpress, ClientVitrine, ClientEcommerce


# Register your models here.
# permet d´enregistrer une table

class AdminClientFormation(admin.ModelAdmin):
    list_display = ('nom', 'lieu_de_naissance', 'email', 'telephone', 'ville', 'profession', 'choix')


admin.site.register(ClientFormation, AdminClientFormation)


class AdminClientWordpress(admin.ModelAdmin):
    list_display = ('statut', 'Nom_client', 'Nom_entreprise', 'telephone', 'email', 'addresses', 'types', 'decryption', 'date_debut',
                    'date_fin', 'zone', 'hebergement')


admin.site.register(ClientWordpress, AdminClientWordpress)


class AdminClientEcommerce(admin.ModelAdmin):
    list_display = ('statut', 'Nom_client', 'Nom_entreprise', 'telephone', 'email', 'addresses', 'types', 'decryption', 'date_debut',
                    'date_fin', 'zone', 'hebergement')

admin.site.register(ClientEcommerce, AdminClientEcommerce)


class AdminClientVitrine(admin.ModelAdmin):
    list_display = ('statut', 'Nom_client', 'Nom_entreprise', 'telephone', 'email', 'addresses', 'types', 'decryption', 'date_debut',
                    'date_fin', 'zone', 'hebergement')

admin.site.register(ClientVitrine, AdminClientVitrine)
