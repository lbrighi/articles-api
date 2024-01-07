from django_filters import rest_framework as filters

from blog.models import Articles


class ArticleFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    category = filters.NumberFilter(field_name='article_category__id')

    class Meta:
        model = Articles
        fields = ['title', 'category']
