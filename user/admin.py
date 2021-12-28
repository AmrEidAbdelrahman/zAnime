from django.contrib import admin
from .models import Profile, Favorit, List, ListItem, Notification
# Register your models here.

admin.site.register(Profile)
admin.site.register(Favorit)
admin.site.register(List)
admin.site.register(ListItem)
admin.site.register(Notification)