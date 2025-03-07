# Generated by Django 5.1.3 on 2025-03-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_music_artist_alter_music_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='is_trending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='music',
            name='popularity',
            field=models.IntegerField(default=0),
        ),
    ]
