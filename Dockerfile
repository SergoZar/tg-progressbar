
# Використовуємо офіційний образ Python
FROM python:3.10

EXPOSE 80
# Додаємо потрібний код у контейнер
COPY . .
WORKDIR .

# Встановлюємо залежності
RUN pip install aiogram pyrogram

# Вказуємо команду для запуску
CMD ["python", "-U ", "usrebot.py"]
