from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.

class Manga(models.Model):
    # ---- TBC ---- #
    PUBLICATION_MONTHLY = "Monthly"
    PUBLICATION_WEEKLY = "Weekly"
    PUBLICATION_DAILY = "Daily"
    PUBLICATION_TYPE = (
        (PUBLICATION_MONTHLY, 'monthly'),
        (PUBLICATION_WEEKLY, 'weekly'),
        (PUBLICATION_DAILY, "daily"),
    )

    TYPE_MANHWA = "Manhwa"
    TYPE_MANGA = "Manga"
    TYPE_COMICS = "Comics"
    TYPE_MANHWA = "Manhua"
    TYPE_NOVEL = "Novel"
    TYPE = (
        (TYPE_MANHWA, 'manhwa'),
        (TYPE_MANHWA, 'manhua'),
        (TYPE_MANGA, 'manga'),
        (TYPE_COMICS, 'comics'),
        (TYPE_NOVEL, 'novel')
    )
    # ------------- #

    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=TYPE, default=TYPE_MANGA)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    publication_date = models.DateField()
    publication_type = models.CharField(max_length=10, choices=PUBLICATION_TYPE, default='seasonal')
    number_of_chapters = models.IntegerField(default=0)

    number_of_members = models.IntegerField(default=0)
    rate = models.FloatField(default=3)

    genres = GenericRelation('ModelGenre')

    def __str__(self):
        return self.title

    def get_genres(self):
        return self.genres.all()


class Genre(models.Model):
    title = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ModelGenre(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='model_tag')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
