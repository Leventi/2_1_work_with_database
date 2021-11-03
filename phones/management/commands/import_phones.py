import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify
from django.db import IntegrityError


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone = Phone(
                phone_id=phone['id'],
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=slugify(phone['name'])
            )

            try:
                phone.save()
                self.stdout.write(self.style.SUCCESS(f'Товар {phone} добавлен в базу'))
            except IntegrityError as e:
                if 'UNIQUE constraint' in e.args[0]:
                    print(f'Товар {phone} уже есть в базе.')
