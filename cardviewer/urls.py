from django.contrib import admin
from django.urls import path, include
from cardviewer import views

urlpatterns = [
    path('', views.home, name='home'),
    path('card/<slug:card_slug>', views.card_view, name='card_view'),

    path('conditions', views.condition_list, name='condition_list'),


]
