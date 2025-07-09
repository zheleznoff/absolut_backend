import os
import uuid
from datetime import datetime
from django.core.exceptions import ValidationError
from django.conf import settings


def get_file_upload_path(instance, filename):
    """
    Создает путь для загрузки файла с сортировкой по годам и месяцам
    Формат: media/YYYY/MM/filename
    """
    # Получаем текущий год и месяц
    now = datetime.now()
    year = now.year
    month = now.month
    
    # Создаем уникальное имя файла для избежания конфликтов
    name, ext = os.path.splitext(filename)
    unique_filename = f"{name}_{uuid.uuid4().hex[:8]}{ext}"
    
    # Возвращаем путь: YYYY/MM/filename
    return f'{year}/{month:02d}/{unique_filename}'


def validate_file_size(value):
    """
    Валидатор для проверки размера файла
    """
    if value.size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError(
            f'Размер файла не может превышать {settings.MAX_UPLOAD_SIZE // (1024*1024)} MB.'
        )


def validate_file_type(value):
    """
    Валидатор для проверки типа файла
    """
    import magic
    
    # Читаем первые 2048 байт для определения MIME-типа
    mime = magic.from_buffer(value.read(2048), mime=True)
    value.seek(0)  # Возвращаем указатель в начало файла
    
    if mime not in settings.ALLOWED_FILE_TYPES:
        raise ValidationError(
            f'Тип файла {mime} не поддерживается. '
            f'Разрешенные типы: {", ".join(settings.ALLOWED_FILE_TYPES)}'
        )


def get_file_extension(filename):
    """
    Получает расширение файла
    """
    return os.path.splitext(filename)[1].lower()


def is_image_file(filename):
    """
    Проверяет, является ли файл изображением
    """
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    return get_file_extension(filename) in image_extensions


def is_document_file(filename):
    """
    Проверяет, является ли файл документом
    """
    document_extensions = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.txt', '.csv']
    return get_file_extension(filename) in document_extensions


def create_year_month_directories():
    """
    Создает директории для текущего года и месяца в MEDIA_ROOT
    """
    now = datetime.now()
    year_dir = os.path.join(settings.MEDIA_ROOT, str(now.year))
    month_dir = os.path.join(year_dir, f"{now.month:02d}")
    
    # Создаем директории, если они не существуют
    os.makedirs(month_dir, exist_ok=True)
    
    return month_dir


def get_file_info(file_path):
    """
    Получает информацию о файле
    """
    if not os.path.exists(file_path):
        return None
    
    stat = os.stat(file_path)
    return {
        'size': stat.st_size,
        'created': datetime.fromtimestamp(stat.st_ctime),
        'modified': datetime.fromtimestamp(stat.st_mtime),
        'extension': get_file_extension(file_path),
    }


def cleanup_old_files(days=30):
    """
    Удаляет старые временные файлы
    """
    import shutil
    from datetime import timedelta
    
    temp_dir = settings.FILE_UPLOAD_TEMP_DIR
    if not os.path.exists(temp_dir):
        return
    
    cutoff_date = datetime.now() - timedelta(days=days)
    
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
            
            if file_modified < cutoff_date:
                try:
                    os.remove(file_path)
                except OSError:
                    pass  # Игнорируем ошибки при удалении 