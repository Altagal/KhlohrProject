from django.contrib import admin
from django.urls import path, include
from cardmaker import views

urlpatterns = [

    path('cart_view', views.cart_view, name='cart_view'),
    path('store-card/<slug:card_slug>', views.store_card_in_cart, name='store_card_in_cart'),
    path('card_print', views.card_print, name='card_print'),
    path('remove_card/<slug:card_slug>', views.remove_stored_card, name='remove_stored_card'),
    path('remove_all_card', views.remove_all_stored_card, name='remove_all_stored_card'),


]
