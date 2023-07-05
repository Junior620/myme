from django.db import models
from django import forms


# Create your models here.

class Client_contact(models.Model):
    nom = models.CharField(max_length=50, null=True, )
    email = models.EmailField(max_length=50)
    telephone = models.FloatField(max_length=50)
    detail = models.TextField(max_length=500)

    class Meta:
        verbose_name = ("Client_contact")
        verbose_name_plural = ("client_contact")

    def __str__(self):
        return self.nom
