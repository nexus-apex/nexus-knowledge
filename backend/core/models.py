from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, default="")
    author = models.CharField(max_length=255, blank=True, default="")
    content = models.TextField(blank=True, default="")
    views = models.IntegerField(default=0)
    helpful = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("draft", "Draft"), ("published", "Published"), ("under_review", "Under Review"), ("archived", "Archived")], default="draft")
    tags = models.CharField(max_length=255, blank=True, default="")
    last_updated = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.CharField(max_length=255, blank=True, default="")
    articles_count = models.IntegerField(default=0)
    position = models.IntegerField(default=0)
    icon = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("hidden", "Hidden")], default="active")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class ArticleComment(models.Model):
    article_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, default="")
    content = models.TextField(blank=True, default="")
    date = models.DateField(null=True, blank=True)
    helpful = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=[("published", "Published"), ("flagged", "Flagged"), ("hidden", "Hidden")], default="published")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.article_title
