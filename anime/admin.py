from django.contrib import admin

# Register your models here.
from chapter.models import Chapter
from comments.models import Comment
from manga.models import Manga
from reviews.models import Review

admin.site.register(Manga)
admin.site.register(Chapter)
admin.site.register(Review)
admin.site.register(Comment)