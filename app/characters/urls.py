from django.urls import path

from characters import views
from characters.apps import CharactersConfig

app_name = CharactersConfig.name

urlpatterns = [
    path("", views.CharactersView.as_view(), name="characters"),
    path("<str:character_id>/quotes/",
         views.QuotesByCharacterView.as_view(), name="quotes_by_character"),

]
