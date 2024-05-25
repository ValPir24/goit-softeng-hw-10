import os
import django

# Налаштування середовища Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes.settings')
django.setup()

import pymongo
import configparser
from quotesapp.models import Author, Quote

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist  # Імпортуємо виняток для обробки випадку відсутності об'єкта

# Читаємо конфігурацію MongoDB
config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

# Підключення до MongoDB
client = pymongo.MongoClient(f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}.utwip5n.mongodb.net/{db_name}?retryWrites=true&w=majority")
mongodb = client["myDB1"]

# Отримання даних з колекцій MongoDB
authors_collection = mongodb["author"]
quotes_collection = mongodb["quote"]

# Створюємо словник для відображення ідентифікаторів авторів MongoDB на Django
author_id_map = {}

# Міграція авторів
for author in authors_collection.find():
    new_author, created = Author.objects.get_or_create(
        fullname=author['fullname'],  # Спробуємо знайти автора за повним ім'ям
        defaults={
            'born_date': author['born_date'],
            'born_location': author['born_location'],
            'description': author['description']
        }
    )
    author_id_map[str(author['_id'])] = new_author.id  # Додаємо відповідний запис у словник

# Міграція цитат
for quote in quotes_collection.find():
    author_id = author_id_map.get(str(quote['author']))  # Отримуємо відповідний ідентифікатор автора зі словника
    if author_id:  # Перевіряємо, чи існує відповідний автор у Django
        existing_quotes = Quote.objects.filter(quote=quote['quote'], author_id=author_id)
        if not existing_quotes:  # Перевіряємо, чи немає вже такої цитати
            # Якщо цитату не знайдено, створюємо нову
            new_quote = Quote(
                quote=quote['quote'],
                author_id=author_id
            )
            new_quote.save()  # Зберігаємо нову цитату

















