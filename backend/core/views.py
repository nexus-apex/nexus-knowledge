import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Article, ArticleCategory, ArticleComment


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['article_count'] = Article.objects.count()
    ctx['article_draft'] = Article.objects.filter(status='draft').count()
    ctx['article_published'] = Article.objects.filter(status='published').count()
    ctx['article_under_review'] = Article.objects.filter(status='under_review').count()
    ctx['articlecategory_count'] = ArticleCategory.objects.count()
    ctx['articlecategory_active'] = ArticleCategory.objects.filter(status='active').count()
    ctx['articlecategory_hidden'] = ArticleCategory.objects.filter(status='hidden').count()
    ctx['articlecomment_count'] = ArticleComment.objects.count()
    ctx['articlecomment_published'] = ArticleComment.objects.filter(status='published').count()
    ctx['articlecomment_flagged'] = ArticleComment.objects.filter(status='flagged').count()
    ctx['articlecomment_hidden'] = ArticleComment.objects.filter(status='hidden').count()
    ctx['recent'] = Article.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def article_list(request):
    qs = Article.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'article_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def article_create(request):
    if request.method == 'POST':
        obj = Article()
        obj.title = request.POST.get('title', '')
        obj.category = request.POST.get('category', '')
        obj.author = request.POST.get('author', '')
        obj.content = request.POST.get('content', '')
        obj.views = request.POST.get('views') or 0
        obj.helpful = request.POST.get('helpful') or 0
        obj.status = request.POST.get('status', '')
        obj.tags = request.POST.get('tags', '')
        obj.last_updated = request.POST.get('last_updated') or None
        obj.save()
        return redirect('/articles/')
    return render(request, 'article_form.html', {'editing': False})


@login_required
def article_edit(request, pk):
    obj = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.category = request.POST.get('category', '')
        obj.author = request.POST.get('author', '')
        obj.content = request.POST.get('content', '')
        obj.views = request.POST.get('views') or 0
        obj.helpful = request.POST.get('helpful') or 0
        obj.status = request.POST.get('status', '')
        obj.tags = request.POST.get('tags', '')
        obj.last_updated = request.POST.get('last_updated') or None
        obj.save()
        return redirect('/articles/')
    return render(request, 'article_form.html', {'record': obj, 'editing': True})


@login_required
def article_delete(request, pk):
    obj = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/articles/')


@login_required
def articlecategory_list(request):
    qs = ArticleCategory.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'articlecategory_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def articlecategory_create(request):
    if request.method == 'POST':
        obj = ArticleCategory()
        obj.name = request.POST.get('name', '')
        obj.parent = request.POST.get('parent', '')
        obj.articles_count = request.POST.get('articles_count') or 0
        obj.position = request.POST.get('position') or 0
        obj.icon = request.POST.get('icon', '')
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/articlecategories/')
    return render(request, 'articlecategory_form.html', {'editing': False})


@login_required
def articlecategory_edit(request, pk):
    obj = get_object_or_404(ArticleCategory, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.parent = request.POST.get('parent', '')
        obj.articles_count = request.POST.get('articles_count') or 0
        obj.position = request.POST.get('position') or 0
        obj.icon = request.POST.get('icon', '')
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/articlecategories/')
    return render(request, 'articlecategory_form.html', {'record': obj, 'editing': True})


@login_required
def articlecategory_delete(request, pk):
    obj = get_object_or_404(ArticleCategory, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/articlecategories/')


@login_required
def articlecomment_list(request):
    qs = ArticleComment.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(article_title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'articlecomment_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def articlecomment_create(request):
    if request.method == 'POST':
        obj = ArticleComment()
        obj.article_title = request.POST.get('article_title', '')
        obj.author = request.POST.get('author', '')
        obj.content = request.POST.get('content', '')
        obj.date = request.POST.get('date') or None
        obj.helpful = request.POST.get('helpful') == 'on'
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/articlecomments/')
    return render(request, 'articlecomment_form.html', {'editing': False})


@login_required
def articlecomment_edit(request, pk):
    obj = get_object_or_404(ArticleComment, pk=pk)
    if request.method == 'POST':
        obj.article_title = request.POST.get('article_title', '')
        obj.author = request.POST.get('author', '')
        obj.content = request.POST.get('content', '')
        obj.date = request.POST.get('date') or None
        obj.helpful = request.POST.get('helpful') == 'on'
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/articlecomments/')
    return render(request, 'articlecomment_form.html', {'record': obj, 'editing': True})


@login_required
def articlecomment_delete(request, pk):
    obj = get_object_or_404(ArticleComment, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/articlecomments/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['article_count'] = Article.objects.count()
    data['articlecategory_count'] = ArticleCategory.objects.count()
    data['articlecomment_count'] = ArticleComment.objects.count()
    return JsonResponse(data)
