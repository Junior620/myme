from django.contrib import admin
from .models import Client_contact


# Register your models here.

class AdminClient_contact(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'detail')


admin.site.register(Client_contact, AdminClient_contact)
