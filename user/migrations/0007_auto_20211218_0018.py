# Generated by Django 3.2 on 2021-12-17 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0007_rename_chapter_number_chapter_chapter_number'),
        ('user', '0006_list_listitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listitem',
            name='manga',
        ),
        migrations.AddField(
            model_name='listitem',
            name='manga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='anime.manga'),
        ),
    ]
