from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from comments.models import Comment
from manga.models import Manga


class Chapter(models.Model):
    title = models.CharField(max_length=255)
    chapter_number = models.IntegerField()
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    season = models.BigIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    publish_time = models.DateTimeField(null=True)

    comments = GenericRelation(Comment, related_query_name='comments')
    # imgs = models.TextField(null=True)

    def __str__(self):
        return f'{self.manga.title} Chapter {self.chapter_number}'

    @property
    def has_next(self):
        n = self.chapter_number + 1
        return Chapter.objects.filter(chapter_number=n).exists()
    @property
    def has_prev(self):
        n = self.chapter_number - 1
        return Chapter.objects.filter(chapter_number=n).exists()
