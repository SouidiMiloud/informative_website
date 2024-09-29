from . import views
from django.urls import path


urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('equipe/', views.equipe, name='equipe'),
    path('preferences/', views.preferences, name='preferences'),
    path('revetements/', views.revetements, name='revetements'),
    path('contact/', views.contact, name='contact'),
]