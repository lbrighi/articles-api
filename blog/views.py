from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from blog.models import Articles, Category
from blog.serializers import ArticleSerializer, CategorySerializer
from user.permissions import IsArticleAccessible


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
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    permission_classes = [IsArticleAccessible]

    def get_queryset(self):
        user = self.request.user

        # Filtra os artigos para mostrar apenas aqueles que estão associados aos grupos do usuário
        queryset = super().get_queryset().filter(
            Q(groups__in=user.groups.all()) | Q(is_all_users=True)
        ).distinct()

        return queryset
