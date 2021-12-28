from django.apps import AppConfig


class AnimeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'anime'


class DjangoNotificationsAppConfig(AppConfig):
    name = 'django_notifications_app'