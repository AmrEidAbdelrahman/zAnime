from django.db import models
from  django.contrib.auth.models import User
from anime.models import Manga
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	pic = models.ImageField(default='default.png', upload_to='profile_images')
	location = models.CharField(max_length=20 , default='Egypt')

	def __str__(self):
		return f'{self.user.username} Profile'


class Favorit(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	manga = models.ForeignKey(Manga, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f'{self.user.username} Likes {self.manga.name}'


class List(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=20)

	def __str__(self):
		return f'{self.user.username} List {self.name}'

class ListItem(models.Model):
	lista = models.ForeignKey(List, on_delete=models.CASCADE)
	manga = models.ForeignKey(Manga, on_delete=models.CASCADE , null=True)

	def __str__(self):
		return f'{self.manga.name} in {self.lista}'

