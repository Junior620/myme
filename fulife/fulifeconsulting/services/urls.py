from django.urls import path,include

#ici on importe les fonctions créeer dans vues
from . import views


urlpatterns = [
    path('reseau-administration', views.reseau_administration, name="reseau&administrtion"),
    path('dev-web-mobile', views.dev_web_mobile, name="dev-web-mobile"),
    path('creation-site-web', views.creation_site_web, name="creation-site-web"),
    path('creation-site-web/formulaire-wordpress', views.formulaire_wordpress, name="formulaire-wordpress"),
    path('creation-site-web/formulaire-vitrine', views.formulaire_vitrine, name="formulaire-vitrine"),
    path('creation-site-web/formulaire-e-commerce', views.formulaire_e_commerce, name="formulaire-e-commerce"),
    path('dev-web-mobile/app-web-mobile', views.app_web_mobile, name="app-web-mobile"),
    path('dev-web-mobile/app-web-mobile/formulaire-app-web-mobile', views.formulaire_app_web_mobile, name="formulaire-app-web-mobile"),
    path('formation/infographe', views.infographe_detail, name="infographe"),
    path('formation/wordpress', views.wordpress_detail, name="wordpress"),
    path('formation/flutter', views.flutter_detail, name="flutter"),
    path('formation/fullstack', views.fullstack_detail, name="fullstack"),
    path('formation/community', views.community_detail, name="community"),
    path('formation/marketing', views.marketing_detail, name="marketing"),
    path('formation/bureautique', views.bureautique_detail, name="bureautique"),
    path('formation/O.S', views.os_detail, name="os"),
    path('hebergement', views.hebergement, name="hebergement"),
    path('hebergement-contact', views.hebergement_contact, name="hebergement-contact"),

    path('formation/inscription', views.inscription_formation, name="inscription-formation"),
]