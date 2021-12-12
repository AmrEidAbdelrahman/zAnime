from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Manga(models.Model):
	## ---- TBC ---- ##
	manga_kinds = [('Advanture','Advanture')]
	manga_pub_type = [('seasonal','seasonal')]
	## ------------- ##

	name = models.CharField(max_length=200)
	description = models.TextField()
	pub_date = models.DateTimeField()
	upload_date = models.DateTimeField(auto_now_add=True)
	## ---- TBC ---- ##
	kind = models.CharField(max_length=10, choices=manga_kinds, default='Advanture')
	pub_type = models.CharField(max_length=10, choices=manga_pub_type, default='seasonal')
	## ------------- ##
	rate = models.IntegerField(default=3)
	number_of_chapters = models.IntegerField()

	def __str__(self):
		return self.name


class Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
	given_rate = models.IntegerField(default=3)
	content = models.TextField()

class Chapter(models.Model):
	manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
	season = models.IntegerField()
	Chapter_number = models.IntegerField()
	pub_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
	content = models.TextField()


