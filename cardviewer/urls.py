from django.contrib import admin
from django.urls import path, include
from cardviewer import views

urlpatterns = [
    path('', views.home, name='home'),
    path('card/<slug:card_slug>', views.card_view, name='card_view'),

    path('spells', views.spell_list, name='spell_list'),
    path('itens', views.item_list, name='item_list'),
    path('infusions', views.infusion_list, name='infusion_list'),
    path('ability-scores-and-skills', views.ability_score_skill_list, name='ability_score_skill_list'),
    path('feats', views.feat_list, name='feat_list'),


]
