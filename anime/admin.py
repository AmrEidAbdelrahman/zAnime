from django.contrib import admin
from .models import Manga, Chapter, Review, Comment, Reply
# Register your models here.

admin.site.register(Manga)
admin.site.register(Chapter)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Reply)