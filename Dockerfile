# Використовуємо офіційний образ Python
FROM python:3.10

# Додаємо потрібний код у контейнер
COPY . .
WORKDIR .

# Встановлюємо залежності
RUN pip install --no-cache-dir aiogram pyrogram

# Вказуємо команду для запуску
CMD ["python", "usrebot.py"]
