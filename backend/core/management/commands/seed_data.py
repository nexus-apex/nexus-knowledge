from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Article, ArticleCategory, ArticleComment
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusKnowledge with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusknowledge.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Article.objects.count() == 0:
            for i in range(10):
                Article.objects.create(
                    title=f"Sample Article {i+1}",
                    category=f"Sample {i+1}",
                    author=f"Sample {i+1}",
                    content=f"Sample content for record {i+1}",
                    views=random.randint(1, 100),
                    helpful=random.randint(1, 100),
                    status=random.choice(["draft", "published", "under_review", "archived"]),
                    tags=f"Sample {i+1}",
                    last_updated=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 Article records created'))

        if ArticleCategory.objects.count() == 0:
            for i in range(10):
                ArticleCategory.objects.create(
                    name=f"Sample ArticleCategory {i+1}",
                    parent=f"Sample {i+1}",
                    articles_count=random.randint(1, 100),
                    position=random.randint(1, 100),
                    icon=f"Sample {i+1}",
                    status=random.choice(["active", "hidden"]),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 ArticleCategory records created'))

        if ArticleComment.objects.count() == 0:
            for i in range(10):
                ArticleComment.objects.create(
                    article_title=f"Sample ArticleComment {i+1}",
                    author=f"Sample {i+1}",
                    content=f"Sample content for record {i+1}",
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    helpful=random.choice([True, False]),
                    status=random.choice(["published", "flagged", "hidden"]),
                )
            self.stdout.write(self.style.SUCCESS('10 ArticleComment records created'))
