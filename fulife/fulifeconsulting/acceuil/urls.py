from django.urls import path,include

#ici on importe les fonctions créeer dans vues
from . import views


urlpatterns = [
    path('acceuil', views.acceuil, name="acceuil")
]