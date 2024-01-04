from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from blog.models import Articles, Category
from blog.serializers import ArticleSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )


class ArticleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
