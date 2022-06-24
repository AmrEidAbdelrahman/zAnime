
from django.db import models

from manga.models import Manga
from user.models import User


class List(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} List {self.name}'


class ListItem(models.Model):
    lista = models.ForeignKey(List, on_delete=models.CASCADE, related_name='listitem_set')
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.manga.title} in {self.lista}'
