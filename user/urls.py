from django.urls import path

from user.views import GroupViewSet, UserViewSet

urlpatterns = [
    path("user/", UserViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "user/<int:pk>/",
        UserViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
    path("group/", GroupViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "group/<int:pk>/",
        GroupViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
]
