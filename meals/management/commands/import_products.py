import json
from django.core.management.base import BaseCommand
from meals.models import Product

class Command(BaseCommand):
    help = 'Импортирует список продуктов из JSON файла'

    def handle(self, *args, **kwargs):
        # Путь к JSON файлу. Можно изменить на свой
        json_file_path = 'products.json'

        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stderr.write(f"Файл {json_file_path} не найден.")
            return
        except json.JSONDecodeError:
            self.stderr.write("Ошибка при чтении JSON.")
            return

        # Импорт данных
        for item in data:
            name = item.get('name')
            calories = item.get('calories')
            if not name or not isinstance(calories, int):
                self.stderr.write(f"Некорректный объект: {item}")
                continue
            Product.objects.create(name=name, calories=calories)
            self.stdout.write(f'Добавлен продукт: {name}')