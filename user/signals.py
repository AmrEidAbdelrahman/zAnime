from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from chapter.models import Chapter
from lists.models import List
from profiles.models import Profile
from .models import Notification


from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
		List.objects.create(user=instance, name=instance.username)


@receiver(post_save,sender=User)
def save_profile(sender, instance, created, **kwargs):
	instance.profile.save()


@receiver(post_save,sender=Chapter)
def send_notification(sender, instance, created, **kwargs):
	if created:
		manga = instance.manga
		all_followers_id = manga.favorit_set.all()
		notifications = []
		for i in all_followers_id:
			notification = Notification.objects.create(user=i.user ,message="New Chapter Notification")
			notifications.append(notification)
		print(notifications)
		if notifications:
			#for i in notifications:
			#	i.save()
			Notification.objects.bulk_create(notifications, ignore_conflicts=True)

		print("##########TESTVIEW###########")
		channel_layer = get_channel_layer()
		async_to_sync(channel_layer.group_send)(
		'event_amr',
		{
			'type': 'receive',
			'message': 'THIS MESSAGE FROM NOTIFICATIONS SIGNAL'
		}
		)
		print("########AFTER TEST VIEW#########")
		print("THIS FUNCTION WORKS GOOD")
		
