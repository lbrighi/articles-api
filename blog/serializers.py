from django.contrib.auth.models import Group
from rest_framework import serializers

from blog.models import ArticleGroup, Articles, Category


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
    is_all_users = serializers.BooleanField(write_only=True)

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
            "is_all_users"
        ]

    def create(self, validated_data):
        article_category = validated_data.pop('article_category').id
        groups = validated_data.pop('groups', [])
        is_all_users = validated_data.pop('is_all_users', False)

        article = Articles.objects.create(article_category_id=article_category, **validated_data)

        for group in groups:
            ArticleGroup.objects.create(articles=article, groups=group, is_all_users=is_all_users)

        return article
