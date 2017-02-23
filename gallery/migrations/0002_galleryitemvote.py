# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryItemVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField()),
                ('time', models.TimeField()),
                ('galleryItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.GalleryItem')),
            ],
        ),
    ]
