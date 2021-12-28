from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self):
        import user.signals


'''
class ChapterConfig(AppConfig):
    name = 'chapter'
    verbose_name = 'Chapter'

    def ready(self):
        import chapter.signals
'''