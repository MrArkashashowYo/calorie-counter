import os
import django

# Укажите путь к файлу настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calorie_counter_settings.settings')  # замените 'tracker.settings' на ваш путь к settings
django.setup()


from meals.models import Product

products = Product.objects.all()
for product in products:
    print(product.name, product.calories)