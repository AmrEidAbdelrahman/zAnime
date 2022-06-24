from django.contrib import admin

# Register your models here.
from profiles.models import Profile, Favorit

admin.site.register(Profile)
admin.site.register(Favorit)
