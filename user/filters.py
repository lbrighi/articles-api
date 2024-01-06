from django_filters import CharFilter, NumberFilter
from django_filters.rest_framework import FilterSet

from user.models import User


class UserFilter(FilterSet):
    pk = NumberFilter(field_name="pk", lookup_expr='exact')
    email = CharFilter(field_name="email", lookup_expr='exact')
    name = CharFilter(field_name="name", lookup_expr='icontains')
    groups = NumberFilter(field_name="groups__id", lookup_expr='exact')

    class Meta:
        model = User
        fields = ['pk', 'email', 'name', 'groups']
