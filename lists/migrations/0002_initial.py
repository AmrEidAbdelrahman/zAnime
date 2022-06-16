# Generated by Django 4.0.5 on 2022-06-16 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lists', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='manga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manga.manga'),
        ),
        migrations.AddField(
            model_name='list',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
