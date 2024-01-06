from django.contrib.auth.models import Group
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Articles(BaseModel):
    title = models.CharField(max_length=350, unique=True)
    article_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    cover_image = ThumbnailerImageField(upload_to='photos', blank=True)
    hightlight = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group)
    description = models.TextField()
    is_all_users = models.BooleanField(default=False)
