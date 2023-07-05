from django.db import models
from django import forms
from django.forms.widgets import CheckboxInput
from django.conf import settings


# Create your models here.


class ClientFormation(models.Model):
    nom = models.CharField(max_length=150, null=True)
    date_naissance = models.DateField(null=True)
    lieu_de_naissance = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telephone = models.CharField(max_length=20, null=True)
    ville = models.CharField(max_length=30)
    profession = models.CharField(max_length=50)
    choix = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = ("ClientFormation")
        verbose_name_plural = ("ClientFormation")

    def __str__(self):
        return self.nom


class ClientWordpress(models.Model):
    statut = models.CharField(max_length=50, null=True)
    Nom_client = models.CharField(max_length=150)
    Nom_entreprise = models.CharField(max_length=150)
    telephone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    addresses = models.CharField(max_length=50)
    types = models.CharField(max_length=50, null=True)
    decryption = models.TextField(max_length=1000)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    zone = models.CharField(max_length=50, null=True)
    hebergement = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = ("ClientWordpress")
        verbose_name_plural = ("ClientWordpress")

    def __str__(self):
        return self.statut


class ClientVitrine(models.Model):
    statut = models.CharField(max_length=50, null=True)
    Nom_client = models.CharField(max_length=150)
    Nom_entreprise = models.CharField(max_length=150)
    telephone = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    addresses = models.CharField(max_length=50)
    types = models.CharField(max_length=50, null=True)
    decryption = models.TextField(max_length=1000)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    zone = models.CharField(max_length=50, null=True)
    hebergement = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = ("ClientVitrine")
        verbose_name_plural = ("ClientVitrine")

    def __str__(self):
        return self.Nom_client


class ClientEcommerce(models.Model):
    statut = models.CharField(max_length=50, null=True)
    Nom_client = models.CharField(max_length=150)
    Nom_entreprise = models.CharField(max_length=150)
    telephone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    addresses = models.CharField(max_length=50)
    types = models.CharField(max_length=50, null=True)
    decryption = models.TextField(max_length=1000)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    zone = models.CharField(max_length=50, null=True)
    hebergement = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = ("ClientEcommerce")
        verbose_name_plural = ("ClientEcommerce")

    def __str__(self):
        return self.Nom_client
