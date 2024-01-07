from django.contrib.auth.models import Group
from django.utils import timezone
from rest_framework import serializers

from blog.models import Articles, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class SmallCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            "id"
        ]


class ArticleSerializer(serializers.ModelSerializer):
    article_category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Articles
        fields = [
            "id",
            "title",
            "article_category",
            "cover_image",
            "hightlight",
            "groups",
            "description",
            "is_all_users",
            "created_at"
        ]

    def create(self, validated_data):
        created_at = validated_data.pop('created_at', None)
        if created_at is None:
            validated_data["created_at"] = timezone.now()

        groups_data = validated_data.pop('groups', [])
        article = Articles.objects.create(**validated_data)

        for group in groups_data:
            article.groups.add(group)

        return article

    def get_article_category(self, article):
        return article.article_category.name if article.article_category else None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['article_category'] = self.get_article_category(instance)
        return representation
