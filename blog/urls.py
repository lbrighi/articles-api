from django.urls import path

from blog.views import ArticleViewSet, CategoryViewSet

urlpatterns = [
    path("category/", CategoryViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "category/<int:pk>/",
        CategoryViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
    path("article/", ArticleViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "article/<int:pk>/",
        ArticleViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
]
