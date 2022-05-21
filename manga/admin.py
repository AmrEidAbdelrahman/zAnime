from django.contrib import admin

# Register your models here.
from manga.models import Manga, Genre, ModelGenre

admin.site.register(Manga)
admin.site.register(Genre)
admin.site.register(ModelGenre)