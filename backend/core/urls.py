from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/create/', views.article_create, name='article_create'),
    path('articles/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('articles/<int:pk>/delete/', views.article_delete, name='article_delete'),
    path('articlecategories/', views.articlecategory_list, name='articlecategory_list'),
    path('articlecategories/create/', views.articlecategory_create, name='articlecategory_create'),
    path('articlecategories/<int:pk>/edit/', views.articlecategory_edit, name='articlecategory_edit'),
    path('articlecategories/<int:pk>/delete/', views.articlecategory_delete, name='articlecategory_delete'),
    path('articlecomments/', views.articlecomment_list, name='articlecomment_list'),
    path('articlecomments/create/', views.articlecomment_create, name='articlecomment_create'),
    path('articlecomments/<int:pk>/edit/', views.articlecomment_edit, name='articlecomment_edit'),
    path('articlecomments/<int:pk>/delete/', views.articlecomment_delete, name='articlecomment_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
