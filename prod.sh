#!/bin/bash
echo "🚀 Запуск продакшен среды..."

# Создаем сеть если её нет
docker network create app_network 2>/dev/null || true

# Запускаем продакшен версию
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d

echo "✅ Продакшен среда запущена!"
echo "🌐 Backend доступен по адресу: http://localhost:8000"
