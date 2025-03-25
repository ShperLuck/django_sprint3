from django.contrib import admin  # Модуль для админки Django

from .models import Category, Location, Post  # Импортируем наши модели из models.py

admin.site.register(Category)  # Регистрируем модель Category в админке
admin.site.register(Location)  # Регистрируем модель Location
admin.site.register(Post)  # Регистрируем модель Post
