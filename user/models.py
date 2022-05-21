from django.db import models
from  django.contrib.auth.models import User
# Create your models here.
from manga.models import Manga


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
		return f'{self.user.username} Likes {self.manga.title}'





class Notification(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	message = models.CharField(max_length=200)
	arr_date = models.DateTimeField(auto_now_add=True)
	arrieved = models.BooleanField(default=False)
	read = models.BooleanField(default=False)
	deleted = models.BooleanField(default=False)


	def __str__(self):
		return f'{self.message}'