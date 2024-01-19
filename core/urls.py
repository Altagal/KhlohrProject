from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('cardmaker.urls')),
    path('', include('cardviewer.urls')),
    path('', include('cardsetting.urls')),

]
