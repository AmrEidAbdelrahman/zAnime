# Generated by Django 3.2 on 2021-12-14 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_auto_20211214_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='number_of_members',
            field=models.IntegerField(default=0),
        ),
    ]
