from django.contrib import admin
from .models import Profile, Favorit, List, ListItem
# Register your models here.

admin.site.register(Profile)
admin.site.register(Favorit)
admin.site.register(List)
admin.site.register(ListItem)