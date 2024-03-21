from django.urls import path
from cardviewer import views

urlpatterns = [
    path('', views.home, name='home'),
    path('card/<slug:card_slug>', views.card_view, name='card_view'),

    path('spells', views.spell_list, name='spell_list'),
    path('magic-itens', views.magic_item_list, name='magic_item_list'),
    path('infusions', views.infusion_list, name='infusion_list'),
    path('ability-scores-and-skills', views.ability_score_skill_list, name='ability_score_skill_list'),
    path('feats', views.feat_list, name='feat_list'),
    path('classes-and-subclasses', views.class_subclass_list, name='class_subclass_list'),
    path('metamagics', views.metamagic_list, name='metamagic_list'),
    path('eldritch-invocations', views.eldritch_invocation_list, name='eldritch_invocation_list'),
    path('battle-maneuvers', views.battle_maneuver_list, name='battle_maneuver_list'),
    path('fighting-styles', views.fighting_style_list, name='fighting_style_list'),
    path('monsters', views.monster_list, name='monster_list'),
    path('armors', views.armor_list, name='armor_list'),
    path('weapons', views.weapon_list, name='weapon_list'),
]
