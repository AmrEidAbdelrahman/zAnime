# Generated by Django 4.0.4 on 2022-05-21 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listitem',
            name='lista',
        ),
        migrations.RemoveField(
            model_name='listitem',
            name='manga',
        ),
        migrations.DeleteModel(
            name='List',
        ),
        migrations.DeleteModel(
            name='ListItem',
        ),
    ]
