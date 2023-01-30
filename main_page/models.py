from django.db import models
import uuid
import os


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', )


class Dishes(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('dishes/', new_filename)

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=300, blank=True)
    ingredients = models.CharField(max_length=300)
    is_visible = models.BooleanField(default=True)
    special = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', 'price', )
        index_together = (('id', 'slug'), )