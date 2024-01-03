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
    category = models.OneToOneField(
        Category,
        on_delete=models.SET_NULL,
        primary_key=True,
    )
    cover_image = ThumbnailerImageField(upload_to='photos', blank=True)
    hightlight = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, through='ArticleGroup')


class ArticleGroup(models.Model):
    articles = models.ForeignKey(Articles, on_delete=models.SET_NULL, null=True, blank=True, related_name='article_group_articles')
    groups = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='article_group_groups')
    is_allowny = models.BooleanField(default=False)
