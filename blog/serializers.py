from django.contrib.auth.models import Group
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
        groups_data = validated_data.pop('groups', [])  # Remova os grupos do validated_data

        # Crie o artigo sem os grupos
        article = Articles.objects.create(**validated_data)

        # Adicione os grupos ao artigo
        for group in groups_data:
            article.groups.add(group)

        return article
