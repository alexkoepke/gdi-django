from django.db import models


class GalleryItem(models.Model):
    image = models.URLField()
    title = models.CharField(max_length=250)
    description = models.TextField(default='')

    def __str__(self):
        return self.title
