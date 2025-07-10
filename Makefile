.PHONY: help dev prod stop clean logs shell migrate test

# Цвета для вывода
GREEN := \033[0;32m
YELLOW := \033[1;33m
RED := \033[0;31m
NC := \033[0m # No Color

ENV_FILE ?= .env.dev

help: ## Показать справку
	@echo "$(GREEN)Доступные команды:$(NC)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  $(YELLOW)%-15s$(NC) %s\n", $$1, $$2}' $(MAKEFILE_LIST)

dev: ## Запустить среду разработки
	@echo "$(GREEN)🚀 Запуск среды разработки...$(NC)"
	@docker network create app_network 2>/dev/null || true
	@docker-compose --env-file $(ENV_FILE) --profile dev up --build -d backend-dev postgres
	@echo "$(GREEN)✅ Среда разработки запущена!$(NC)"
	@echo "$(YELLOW)🌐 Backend: http://localhost:$$(grep BACKEND_DEV_PORT $(ENV_FILE) | cut -d '=' -f2 | tr -d '\r' | tail -1 || echo 8000)$(NC)"

prod: ## Запустить продакшен среду
	@echo "$(GREEN)🚀 Запуск продакшен среды...$(NC)"
	@docker network create app_network 2>/dev/null || true
	@docker-compose --env-file $(ENV_FILE) -f docker-compose.yml -f docker-compose.prod.yml up --build -d
	@echo "$(GREEN)✅ Продакшен среда запущена!$(NC)"

stop: ## Остановить все контейнеры
	@echo "$(YELLOW)🛑 Остановка контейнеров...$(NC)"
	@docker-compose --profile dev down
	@docker-compose -f docker-compose.yml -f docker-compose.prod.yml down
	@echo "$(GREEN)✅ Контейнеры остановлены$(NC)"

clean: ## Очистить все (контейнеры, образы, volumes)
	@echo "$(RED)🧹 Очистка всех данных...$(NC)"
	@docker-compose --profile dev down -v --remove-orphans
	@docker-compose -f docker-compose.yml -f docker-compose.prod.yml down -v --remove-orphans
	@docker system prune -f
	@echo "$(GREEN)✅ Очистка завершена$(NC)"

logs: ## Показать логи
	@docker-compose logs -f

logs-backend: ## Показать логи backend
	@docker-compose logs -f backend

logs-db: ## Показать логи базы данных
	@docker-compose logs -f postgres

shell: ## Зайти в shell контейнера backend
	@docker-compose exec backend bash

shell-db: ## Зайти в shell базы данных
	@docker-compose exec postgres psql -U postgres -d postgres

migrate: ## Выполнить миграции
	@echo "$(GREEN)🔄 Выполнение миграций...$(NC)"
	@docker-compose exec backend python src/manage.py migrate
	@echo "$(GREEN)✅ Миграции выполнены$(NC)"

makemigrations: ## Создать миграции
	@echo "$(GREEN)📝 Создание миграций...$(NC)"
	@docker-compose exec backend python src/manage.py makemigrations
	@echo "$(GREEN)✅ Миграции созданы$(NC)"

collectstatic: ## Собрать статические файлы
	@echo "$(GREEN)📦 Сбор статических файлов...$(NC)"
	@docker-compose exec backend python src/manage.py collectstatic --noinput
	@echo "$(GREEN)✅ Статические файлы собраны$(NC)"

test: ## Запустить тесты
	@echo "$(GREEN)🧪 Запуск тестов...$(NC)"
	@docker-compose exec backend python src/manage.py test
	@echo "$(GREEN)✅ Тесты завершены$(NC)"

superuser: ## Создать суперпользователя
	@echo "$(GREEN)👤 Создание суперпользователя...$(NC)"
	@docker-compose exec backend python src/manage.py createsuperuser

backup-db: ## Создать бэкап базы данных
	@echo "$(GREEN)💾 Создание бэкапа базы данных...$(NC)"
	@docker-compose exec postgres pg_dump -U postgres postgres > backup_$(shell date +%Y%m%d_%H%M%S).sql
	@echo "$(GREEN)✅ Бэкап создан$(NC)"

restore-db: ## Восстановить базу данных (файл backup.sql)
	@echo "$(GREEN)🔄 Восстановление базы данных...$(NC)"
	@docker-compose exec -T postgres psql -U postgres postgres < backup.sql
	@echo "$(GREEN)✅ База данных восстановлена$(NC)"

build: ## Пересобрать образы
	@echo "$(GREEN)🔨 Пересборка образов...$(NC)"
	@docker-compose build --no-cache
	@echo "$(GREEN)✅ Образы пересобраны$(NC)"

status: ## Показать статус контейнеров
	@echo "$(GREEN)📊 Статус контейнеров:$(NC)"
	@docker-compose ps

# Примеры использования:
# make dev      - запустить разработку
# make prod     - запустить продакшен
# make stop     - остановить все
# make logs     - показать логи
# make shell    - зайти в backend контейнер
# make migrate  - выполнить миграции