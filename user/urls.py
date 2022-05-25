from django.urls import path, include
from user import views as user_views

from anime.views import Favlist
from manga.views import MangaView

app_name = 'manga'
urlpatterns = [
    path('favlist/', Favlist, name='fav-list'),
    path('profile/', user_views.profile, name='profile'),
]
