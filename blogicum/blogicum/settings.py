from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Создаем пути внутри проекта, например: BASE_DIR / 'подпапка'.
BASE_DIR = Path(__file__).resolve().parent.parent  # BASE_DIR - это корневая директория проекта

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
# Быстрые настройки для разработки - не подходят для продакшна
# Смотрите https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# ВНИМАНИЕ: храните секретный ключ, используемый в продакшене, в секрете!
SECRET_KEY = 'django-insecure-xn5)z4fdefk$^j!_&-!xukk-d@@eprv!nes2l_wp5f2=6_!l(a'  # Секретный ключ для защиты проекта

# SECURITY WARNING: don't run with debug turned on in production!
# ВНИМАНИЕ: не запускайте с включенным дебагом в продакшене!
DEBUG = True  # Включает режим отладки

ALLOWED_HOSTS = []  # Список разрешенных хостов

# Application definition
# Определение приложений

STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Путь к папке со статическими файлами
]

INSTALLED_APPS = [
    'django.contrib.admin',  # Приложение администрирования Django
    'django.contrib.auth',  # Приложение аутентификации Django
    'django.contrib.contenttypes',  # Приложение управления типами контента Django
    'django.contrib.sessions',  # Приложение управления сессиями Django
    'django.contrib.messages',  # Приложение управления сообщениями Django
    'django.contrib.staticfiles',  # Приложение управления статическими файлами Django
    'blog.apps.BlogConfig',  # Конфигурация приложения blog
    'pages.apps.PagesConfig',  # Конфигурация приложения pages
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Middleware для защиты
    'django.contrib.sessions.middleware.SessionMiddleware',  # Middleware для работы с сессиями
    'django.middleware.common.CommonMiddleware',  # Общий middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # Middleware для защиты от CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Middleware для аутентификации
    'django.contrib.messages.middleware.MessageMiddleware',  # Middleware для работы с сообщениями
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Middleware для защиты от clickjacking
]

ROOT_URLCONF = 'blogicum.urls'  # Главный файл URL-ов проекта

TEMPLATES_DIR = BASE_DIR / 'templates'  # Путь к папке с шаблонами

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Используемый бэкенд для шаблонов
        'DIRS': [TEMPLATES_DIR],  # Пути, где искать шаблоны
        'APP_DIRS': True,  # Искать шаблоны в папках приложений
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Добавляет переменную debug в контекст шаблонов
                'django.template.context_processors.request',  # Добавляет объект request в контекст шаблонов
                'django.contrib.auth.context_processors.auth',  # Добавляет переменные аутентификации в контекст шаблонов
                'django.contrib.messages.context_processors.messages',  # Добавляет сообщения в контекст шаблонов
            ],
        },
    },
]

WSGI_APPLICATION = 'blogicum.wsgi.application'  # Путь к WSGI приложению

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# Настройки базы данных
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Используемая СУБД
        'NAME': BASE_DIR / 'db.sqlite3',  # Имя файла базы данных
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
# Настройки валидации пароля
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Валидатор схожести с пользовательскими атрибутами
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Валидатор минимальной длины пароля
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Валидатор распространенных паролей
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Валидатор паролей только из цифр
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
# Настройки интернационализации
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'  # Код языка

TIME_ZONE = 'UTC'  # Часовой пояс

USE_I18N = True  # Использовать интернационализацию

USE_L10N = True  # Использовать локализацию

USE_TZ = True  # Использовать часовые пояса

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# Настройки статических файлов (CSS, JavaScript, изображения)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'  # URL для доступа к статическим файлам

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
# Тип первичного ключа по умолчанию
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Тип поля для автогенерируемых первичных ключей
