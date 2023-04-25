from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def to_dict_json(self):
        return {
            'name': self.name,
            'slug': self.slug,
        }
