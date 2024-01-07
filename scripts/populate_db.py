import random
from random import choice

from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Articles, Category
from user.models import User

fake = Faker(['en-US', 'en_US', 'en_US', 'en-US'])


class Command(BaseCommand):
    help = 'Popula o banco de dados com dados de exemplo'

    def create_articles_for_category(self, category, groups, num_articles=10):
        days_between_creation = 10
        image_prefix = category.name.lower()

        for _ in range(num_articles):
            created_at = fake.date_time_between(start_date=f"-{days_between_creation}d", end_date="now")

            category_images = [img for img in images if img.startswith(image_prefix)]

            cover_image = fake.random_element(elements=category_images)

            article = Articles.objects.create(
                title=fake.sentence(),
                article_category=category,
                cover_image=f"photos/{cover_image}.jpg",
                hightlight=fake.boolean(chance_of_getting_true=20),
                description=fake.text(max_nb_chars=2000),
                created_at=created_at
            )

            random_group = choice(groups)
            article.groups.add(random_group)

            if random.random() < 0.7:
                article.is_all_users = True
                article.save()

    def run(self, *args, **kwargs):
        group2, created = Group.objects.get_or_create(name='leitores')
        group1, created = Group.objects.get_or_create(name='assinantes')
        group3, created = Group.objects.get_or_create(name='editores')
        group4, created = Group.objects.get_or_create(name='administradores')

        superuser, created = User.objects.get_or_create(
            name='teste',
            email='teste@email.com',
            is_staff=True,
            is_superuser=True
        )

        superuser.set_password('123456')
        superuser.save()
        for _ in range(5):
            user, created = User.objects.get_or_create(
                email=fake.email(),
                name=fake.name(),
                is_active=True
            )
            user.set_password('123456')
            user.groups.add(choice([group1, group2, group3, group4]))

        category1, created = Category.objects.get_or_create(name='Esporte')
        category2, created = Category.objects.get_or_create(name='Culinaria')
        category3, created = Category.objects.get_or_create(name='Politica')
        category4, created = Category.objects.get_or_create(name='Viagem')

        groups = [group1, group2, group3, group4]
        self.create_articles_for_category(category1, groups)
        self.create_articles_for_category(category2, groups)
        self.create_articles_for_category(category3, groups)
        self.create_articles_for_category(category4, groups)

        self.stdout.write(self.style.SUCCESS('Dados populados com sucesso!'))


images = [
    'culinaria', 'culinaria1', 'culinaria2', 'culinaria3', 'culinaria4', 'culinaria5', 'culinaria6', 'culinaria7', 'culinaria8', 'culinaria9',
    'esporte', 'esporte1', 'esporte2', 'esporte3', 'esporte4', 'esporte5', 'esporte6', 'esporte7', 'esporte8', 'esporte9',
    'politica', 'politica1', 'politica2', 'politica3', 'politica4', 'politica5', 'politica6', 'politica7', 'politica8', 'politica9',
    'viagem', 'viagem1', 'viagem2', 'viagem3', 'viagem4', 'viagem5', 'viagem6', 'viagem7', 'viagem8', 'viagem9',
]


def run():
    Command().run()
