# Используем официальный Python образ с тегом slim-buster
FROM python:3.9-slim-buster

# Устанавливаем зависимости
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Копируем проект в контейнер
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Указываем команду для запуска сервера Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "TestDevOps.wsgi:application"]
