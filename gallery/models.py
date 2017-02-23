from django.db import models


class GalleryItem(models.Model):
    image = models.URLField()
    title = models.CharField(max_length=250)
    description = models.TextField(default='')

    def __str__(self):
        return self.title


class Vote(models.Model):
    gallery_item = models.ForeignKey('GalleryItem')
    vote = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Vote for {item}'.format(self.gallery_item.title)
