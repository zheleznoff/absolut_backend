# Backend Project

Django проект с настройкой PostgreSQL через переменные окружения.

## Быстрый старт с Docker

1. Запустите PostgreSQL в Docker:
```bash
docker-compose -f docker-compose/storages.yml up -d postgres
```

2. Скопируйте настройки для Docker:
```bash
cp env.docker .env
```

3. Установите зависимости:
```bash
cd backend
uv sync
```

4. Выполните миграции:
```bash
python src/manage.py migrate
```

5. Создайте суперпользователя:
```bash
python src/manage.py createsuperuser
```

6. Запустите сервер разработки:
```bash
python src/manage.py runserver
```

## Остановка Docker контейнеров

```bash
docker-compose -f docker-compose/storages.yml down
```

Для удаления данных базы данных:
```bash
docker-compose -f docker-compose/storages.yml down -v
```

## Установка и настройка

### Вариант 1: С Docker (рекомендуется)

1. Запустите PostgreSQL в Docker:
```bash
docker-compose -f docker-compose/storages.yml up -d postgres
```

2. Скопируйте настройки для Docker:
```bash
cp env.docker .env
```

3. Перейдите в папку backend и установите зависимости:
```bash
cd backend
uv sync
```

### Вариант 2: Локальная установка PostgreSQL

1. Установите PostgreSQL локально
2. Создайте базу данных и пользователя
3. Скопируйте настройки:
```bash
cp env.example .env
```
4. Отредактируйте `.env` файл под ваши настройки

### Общие шаги после настройки БД

1. Установите зависимости:
```bash
uv sync
```

**Примечание**: Если вы используете pip вместо uv:
```bash
pip install -r requirements.txt
```

2. Убедитесь, что PostgreSQL запущен и доступен

3. Выполните миграции:
```bash
python src/manage.py migrate
```

6. Создайте суперпользователя:
```bash
python src/manage.py createsuperuser
```

7. Запустите сервер разработки:
```bash
python src/manage.py runserver
```

## Переменные окружения

- `SECRET_KEY` - секретный ключ Django (по умолчанию используется встроенный ключ для разработки)
- `DEBUG` - режим отладки (True/False)
- `DB_NAME` - имя базы данных PostgreSQL
- `DB_USER` - пользователь базы данных
- `DB_PASSWORD` - пароль пользователя базы данных
- `DB_HOST` - хост базы данных
- `DB_PORT` - порт базы данных

## Безопасность

⚠️ **Внимание**: В продакшене обязательно:
- Измените `SECRET_KEY` на уникальный
- Установите `DEBUG=False`
- Настройте `ALLOWED_HOSTS` для конкретных доменов
- Используйте безопасные пароли для базы данных
