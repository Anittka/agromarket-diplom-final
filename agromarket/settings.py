from pathlib import Path
import os

from dotenv import load_dotenv
import dj_database_url

# =========================================================
# Загрузка переменных окружения из .env
# =========================================================
load_dotenv()

# =========================================================
# Базовая директория проекта
# =========================================================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================================================
# Безопасность
# =========================================================

# SECRET_KEY:
# В production Render будет брать ключ из Environment Variables
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-agromarket-diplom-local-key'
)

# DEBUG:
# True только локально
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# =========================================================
# Разрешённые хосты
# =========================================================

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv(
        'ALLOWED_HOSTS',
        '127.0.0.1,localhost,.onrender.com'
    ).split(',')
    if host.strip()
]

# Автоматическое добавление Render домена
if os.environ.get('RENDER_EXTERNAL_HOSTNAME'):
    ALLOWED_HOSTS.append(
        os.environ.get('RENDER_EXTERNAL_HOSTNAME')
    )

# =========================================================
# Установленные приложения
# =========================================================

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'siteapp',
]

# =========================================================
# Middleware
# =========================================================

MIDDLEWARE = [
    # Безопасность
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise нужен для статики на Render
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    # CSRF защита
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # Защита iframe
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =========================================================
# URL и WSGI
# =========================================================

ROOT_URLCONF = 'agromarket.urls'

WSGI_APPLICATION = 'agromarket.wsgi.application'

# =========================================================
# Шаблоны
# =========================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Дополнительные папки шаблонов
        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Глобальные настройки сайта
                'siteapp.context_processors.site_settings',
            ],
        },
    },
]

# =========================================================
# База данных
# =========================================================

# Render автоматически передаёт DATABASE_URL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# =========================================================
# Локализация
# =========================================================

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# =========================================================
# Статические файлы
# =========================================================

STATIC_URL = '/static/'

# Папка для collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise storage
STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)

# =========================================================
# Медиафайлы
# =========================================================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# =========================================================
# Primary key
# =========================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =========================================================
# Безопасность
# =========================================================

CSRF_TRUSTED_ORIGINS = [
    url.strip()
    for url in os.getenv(
        'CSRF_TRUSTED_ORIGINS',
        ''
    ).split(',')
    if url.strip()
]

SECURE_CONTENT_TYPE_NOSNIFF = True

SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_HTTPONLY = True

# Secure cookies только в production
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

# HTTPS redirect
SECURE_SSL_REDIRECT = (
    os.getenv('SECURE_SSL_REDIRECT', 'False') == 'True'
)

# HSTS
SECURE_HSTS_SECONDS = int(
    os.getenv('SECURE_HSTS_SECONDS', '0')
)

SECURE_HSTS_INCLUDE_SUBDOMAINS = (
    os.getenv(
        'SECURE_HSTS_INCLUDE_SUBDOMAINS',
        'False'
    ) == 'True'
)

SECURE_HSTS_PRELOAD = (
    os.getenv(
        'SECURE_HSTS_PRELOAD',
        'False'
    ) == 'True'
)

# =========================================================
# Ограничения загрузки файлов
# =========================================================

DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024

FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024

# =========================================================
# Email
# =========================================================

EMAIL_BACKEND = os.getenv(
    'EMAIL_BACKEND',
    'django.core.mail.backends.console.EmailBackend'
)

DEFAULT_FROM_EMAIL = os.getenv(
    'DEFAULT_FROM_EMAIL',
    'site@agromarket.local'
)

ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', '')

# =========================================================
# Папка для резервных копий
# =========================================================

BACKUP_DIR = BASE_DIR / 'backups'

if not BACKUP_DIR.exists():
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

# =========================================================
# Разрешение iframe
# =========================================================

X_FRAME_OPTIONS = 'SAMEORIGIN'
