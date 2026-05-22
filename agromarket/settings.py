from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

# Загружаем переменные окружения из .env
load_dotenv()

# Главная директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ Django
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-agromarket-key'
)

# Режим разработки
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# Разрешённые хосты
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.onrender.com',
]

# Если сайт работает на Render — автоматически добавляем домен
RENDER_EXTERNAL_HOSTNAME = os.getenv('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# =========================
# INSTALLED APPS
# =========================

INSTALLED_APPS = [
    # Стандартные Django приложения
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Наше приложение
    'siteapp',
]

# =========================
# MIDDLEWARE
# =========================

MIDDLEWARE = [
    # Безопасность Django
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise для статики на Render
    'whitenoise.middleware.WhiteNoiseMiddleware',

    # Сессии
    'django.contrib.sessions.middleware.SessionMiddleware',

    # Общие middleware
    'django.middleware.common.CommonMiddleware',

    # CSRF защита
    'django.middleware.csrf.CsrfViewMiddleware',

    # Авторизация
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # Сообщения
    'django.contrib.messages.middleware.MessageMiddleware',

    # Защита iframe
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =========================
# URLS
# =========================

ROOT_URLCONF = 'agromarket.urls'

# =========================
# TEMPLATES
# =========================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Дополнительные папки шаблонов
        'DIRS': [],

        # Автопоиск templates
        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                # Request
                'django.template.context_processors.request',

                # Авторизация
                'django.contrib.auth.context_processors.auth',

                # Сообщения
                'django.contrib.messages.context_processors.messages',

                # Настройки сайта
                'siteapp.context_processors.site_settings',
            ],
        },
    },
]

# =========================
# WSGI
# =========================

WSGI_APPLICATION = 'agromarket.wsgi.application'

# =========================
# DATABASE
# PostgreSQL для Render
# =========================

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

# =========================
# LANGUAGE
# =========================

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# =========================
# STATIC FILES
# =========================

STATIC_URL = '/static/'

# Папка собранной статики
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise storage
STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)

# =========================
# MEDIA FILES
# =========================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# =========================
# DEFAULT AUTO FIELD
# =========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =========================
# SECURITY
# =========================

X_FRAME_OPTIONS = 'SAMEORIGIN'

SECURE_CONTENT_TYPE_NOSNIFF = True

SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_HTTPONLY = True

# HTTPS cookies на production
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

# SSL redirect
SECURE_SSL_REDIRECT = False

# =========================
# CSRF TRUSTED ORIGINS
# =========================

CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
]

# =========================
# FILE UPLOAD LIMITS
# =========================

DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024

FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024

# =========================
# EMAIL
# =========================

EMAIL_BACKEND = os.getenv(
    'EMAIL_BACKEND',
    'django.core.mail.backends.console.EmailBackend'
)

DEFAULT_FROM_EMAIL = os.getenv(
    'DEFAULT_FROM_EMAIL',
    'site@agromarket.local'
)

ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', '')

# =========================
# BACKUPS
# =========================

BACKUP_DIR = BASE_DIR / 'backups'

if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)
