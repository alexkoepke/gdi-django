# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 00:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_galleryitemvote'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GalleryItemVote',
            new_name='Vote',
        ),
    ]
