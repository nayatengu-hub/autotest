FROM mcr.microsoft.com/playwright/python:v1.61.0-jammy

# Переводим установщик в полностью автоматический режим без лишних пакетов
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    xvfb \
    x11vnc \
    novnc \
    websockify \
    && rm -rf /var/lib/apt/lists/*

# Настройка рабочей директории
WORKDIR /app

# Копирование и установка зависимостей Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода проекта
COPY . .

ENV PYTHONPATH=/app

# Открываем порты: 5900 (для обычного VNC) и 8080 (для noVNC в браузере)
EXPOSE 5900 8080

# Скрипт автоматического запуска
CMD bash -c " \
    Xvfb :1 -screen 0 1280x1024x24 & \
    export DISPLAY=:1 && \
    sleep 2 && \
    x11vnc -display :1 -forever -shared -nopw -rfbport 5900 & \
    /usr/share/novnc/utils/launch.sh --vnc localhost:5900 --listen 8080 & \
    sleep 2 && \
    pytest \
    "