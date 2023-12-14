from typing import Any
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write('Создание новых типов товаров')
        self.stdout.write(self.style.SUCCESS('Новые типы товаров были успешно созданы'))
        
