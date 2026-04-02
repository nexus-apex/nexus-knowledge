from django.contrib import admin
from .models import Article, ArticleCategory, ArticleComment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "views", "helpful", "created_at"]
    list_filter = ["status"]
    search_fields = ["title", "category", "author"]

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "parent", "articles_count", "position", "icon", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "parent", "icon"]

@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ["article_title", "author", "date", "helpful", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["article_title", "author"]
