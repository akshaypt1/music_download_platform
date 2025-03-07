# Generated by Django 5.1.3 on 2025-02-27 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='artists/')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='albums/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='music/')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genre')),
            ],
        ),
    ]
