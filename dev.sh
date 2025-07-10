echo "🚀 Запуск среды разработки..."

# Создаем сеть если её нет
docker network create app_network 2>/dev/null || true

# Запускаем только необходимые сервисы для разработки
docker-compose --profile dev up --build -d

echo "✅ Среда разработки запущена!"
echo "🌐 Backend доступен по адресу: http://localhost:8000"
echo "📊 База данных: postgres://postgres:postgres123@localhost:5432/absolut_dev"
