from django.contrib import admin

from chapter.models import Chapter
from comments.models import Comment
from manga.models import Manga, Genre, ModelGenre
from reviews.models import Review

admin.site.register(Manga)
admin.site.register(Chapter)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(ModelGenre)

