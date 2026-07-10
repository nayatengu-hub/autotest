FROM mcr.microsoft.com/playwright/python:v1.45.0-jammy

# Установка системных зависимостей, в том числе xvfb для виртуального дисплея (в официальном образе xvfb уже есть, но перестрахуемся)
RUN apt-get update && apt-get install -y \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /app

# Копирование файла с зависимостями
COPY requirements.txt .

# Установка Python зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода проекта
COPY . .

# Настройка PYTHONPATH (чтобы pytest видел наши модули)
ENV PYTHONPATH=/app

# Команда для запуска тестов с виртуальным дисплеем. Разделяем аргументы правильно!
CMD ["xvfb-run", "--auto-servernum", "--server-args=-screen 0 1920x1080x24", "pytest", "tests/", "--alluredir=allure-results"]
