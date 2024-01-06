from rest_framework import permissions


class IsArticleAccessible(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.is_all_users:
            return True

        user_groups = request.user.groups.all()
        article_groups = obj.groups.all()

        return any(group in user_groups for group in article_groups)
