from django.db import models
from django.contrib.auth.models import User
import time
# Create your models here.

'''
TO ADD THE DATA FROM CSV FILE
for i in range(2,99):
    ...:     m = list(df.iloc[i].values)[1:]
    ...:     manga = Manga(name=m[0], description=m[1], rate=m[2], number_of_members=int(m[3].replace(",","")))
    ...:     manga.save()


'''


class Manga(models.Model):
	## ---- TBC ---- ##
	manga_kinds = [('Advanture','Advanture')]
	manga_pub_type = [('seasonal','seasonal')]
	## ------------- ##

	name = models.CharField(max_length=200)
	description = models.TextField()
	## ---- TBC ---- ##
	## pub_date = models.DateField()
	## ------------- ##
	upload_date = models.DateTimeField(auto_now_add=True)
	## ---- TBC ---- ##
	genres = models.CharField(max_length=10, default='Advanture')
	pub_type = models.CharField(max_length=10, choices=manga_pub_type, default='seasonal')
	## ------------- ##
	## ---- TBC ---- ##
	## ADD THE MANGA PROFILE IMAGE
	## ------------- ##
	number_of_members = models.IntegerField(default=0)
	rate = models.FloatField(default=3)
	number_of_chapters = models.IntegerField(default=0)

	def __str__(self):
		return self.name

	def genres_as_list(self):
		return self.genres.split(',')

class Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
	given_rate = models.IntegerField(default=3)
	content = models.TextField()

class Chapter(models.Model):
	manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
	season = models.IntegerField(default=1)
	chapter_number = models.IntegerField()
	pub_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f'{self.manga.name} Chapter {self.chapter_number}'

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
	content = models.TextField()


