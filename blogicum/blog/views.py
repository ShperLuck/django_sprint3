from datetime import datetime  # Это чтобы работать с датой и временем

# Функции для работы со страницами
from django.shortcuts import render, get_object_or_404

from .models import Post, Category  # Модели, чтобы брать данные из базы


def posts():
    """Достаём посты из базы"""
    # только нужные посты
    # что такое select_related
    return Post.objects.select_related(
        'category',  # Берем категорию
        'location',  # Берем локацию
        'author'  # Берем автора
    ).filter(
        is_published=True,  # Только опубликованные посты
        category__is_published=True,  # Категория тоже должна быть опубликована
        pub_date__lte=datetime.now()  # Дата публикации не позже сегодняшней
    )


def index(request):
    """Показываем главную страницу с постами"""
    post_list = posts()[:5]  # Берем первые 5 постов
    return render(request, 'blog/index.html', {'post_list': post_list})
    # post_list — это список постов для шаблона


def post_detail(request, id):
    """Показываем страницу одного поста"""
    post = get_object_or_404(
        posts(), id=id)  # Берем пост по id, если нет — 404
    return render(request, 'blog/detail.html', {'post': post})
    # get_object_or_404


def category_posts(request, category_slug):
    """Показываем посты одной категории"""
    category = get_object_or_404(
        Category,  # Берем категорию
        slug=category_slug,  # По её слагу
        is_published=True  # Только если она опубликована
    )
    post_list = posts().filter(category=category)  # Берем посты этой категории
    context = {'category': category,
               'post_list': post_list}  # Передаем в шаблон
    return render(request, 'blog/category.html', context)
