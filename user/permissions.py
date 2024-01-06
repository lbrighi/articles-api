from rest_framework import permissions


class IsArticleAccessible(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Se is_all_users for True, todos os usuários têm permissão
        if obj.is_all_users:
            return True

        # Se não for is_all_users, verifica se o usuário pertence a pelo menos um dos grupos associados ao artigo
        user_groups = request.user.groups.all()
        article_groups = obj.groups.all()

        return any(group in user_groups for group in article_groups)
