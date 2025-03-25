from django.contrib.auth import get_user_model  # Функция для получения модели юзера
from django.db import models  # Модуль для создания моделей, это как таблицы в базе

User = get_user_model()  # Берём модель юзера из настроек
TEXT_LENGTH = 256  # Константа для максимальной длины текста, типа лимит символов

class BaseModel(models.Model):  # Базовая модель, чтобы не повторять код
    is_published = models.BooleanField(  # Поле для включения/выключения публикации
        default=True,  # По умолчанию включено
        verbose_name='Опубликовано',  # Название в админке
        help_text='Снимите галочку, чтобы скрыть публикацию.'  # Подсказка
    )
    created_at = models.DateTimeField(  # Поле для даты создания
        auto_now_add=True,  # Ставит дату автоматически при создании
        verbose_name='Добавлено'  # Название в админке
    )

    class Meta:  # Настройки модели
        abstract = True  # Делаем абстрактной, чтобы использовать как основу



class Category(BaseModel):  # Модель для категорий, наследуем от BaseModel
    title = models.CharField(max_length=TEXT_LENGTH, verbose_name='Заголовок')  # Название категории
    description = models.TextField(verbose_name='Описание')  # Описание, длинный текст
    slug = models.SlugField(  # Уникальный идентификатор для URL
        unique=True,  # Не может повторяться
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы '
                  'латиницы, цифры, дефис и подчёркивание.'
    )

    class Meta:  # Настройки
        verbose_name = 'категория'  # Имя в админке
        verbose_name_plural = 'Категории'  # Множественное число

# уточнять про slug

class Location(BaseModel):  # Модель для местоположений
    name = models.CharField(max_length=TEXT_LENGTH, verbose_name='Название места')  # Название места

    class Meta:  # Настройки
        verbose_name = 'местоположение'  # Имя в админке
        verbose_name_plural = 'Местоположения'  # Множественное число

class Post(BaseModel):  # Модель для постов
    title = models.CharField(max_length=TEXT_LENGTH, verbose_name='Заголовок')  # Заголовок поста
    text = models.TextField(verbose_name='Текст')  # Текст поста
    pub_date = models.DateTimeField(  # Дата публикации
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — '
                  'можно делать отложенные публикации.'
    )
    author = models.ForeignKey(  # Связь с автором
        User,  # Модель юзера
        on_delete=models.CASCADE,  # Если юзер удалён, посты тоже
        verbose_name='Автор публикации',
        related_name='posts'  # Обратная связь, чтобы взять все посты юзера
    )
    location = models.ForeignKey(  # Связь с местом
        Location,
        on_delete=models.SET_NULL,  # Если место удалено, поле станет пустым
        null=True,  # Можно оставить пустым
        verbose_name='Местоположение',
        related_name='posts'  # Обратная связь для постов по месту
    )
    category = models.ForeignKey(  # Связь с категорией
        Category,
        on_delete=models.SET_NULL,  # Категория может стать пустой
        null=True,  # Можно не указывать
        verbose_name='Категория',
        related_name='posts'  # Обратная связь для постов по категории
    )

    class Meta:  # Настройки
        verbose_name = 'публикация'  # Имя в админке
        verbose_name_plural = 'Публикации'  # Множественное число
        ordering = ['-pub_date']  # Сортировка по дате, от новых к старым

