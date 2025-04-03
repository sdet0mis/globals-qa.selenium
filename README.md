# Cервис API

Данный сервис предоставляет точки доступа для управления сущностями в базе данных PostgreSQL. Включает конфигурацию Docker Compose для настройки сервиса, базы данных и миграций.

## Начало работы

1. Клонируйте данный репозиторий.
2. Установите Docker и Docker Compose, если они еще не установлены.

## Использование

Для запуска сервиса, базы данных и миграций, перейдите в каталог проекта и выполните:

```make run``` или ```docker-compose up --build -d```

Для запуска тестов и генерации отчета о тестировании выполните:

```pytest -n 5 --alluredir=allure-results``` и ```allure generate --single-file allure-results --clean```

## Точки доступа API

- Создание сущности: POST /api/create
- Удаление сущности: DELETE /api/delete/{id}
- Получение сущности: GET /api/get/{id}
- Получение всех сущностей: POST /api/getAll
- Обновление сущности: PATCH /api/patch/{id}
  
  
#### HOST http://localhost:8080
#### SWAGGER документация http://localhost:8080/api/_/docs/swagger/