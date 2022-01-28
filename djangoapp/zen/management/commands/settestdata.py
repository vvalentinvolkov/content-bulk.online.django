import datetime

from django.core.management import BaseCommand
from django.db import IntegrityError
from faker import Faker
from progress.bar import Bar

from ...models import ZenArticle, ZenFeed

fake = Faker()
ru_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


class Command(BaseCommand):
    help = 'Create test zen articles (Faker)'

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int)

    def handle(self, *args, **options):
        if options.get('number') is None:
            options['number'] = 1
        bar = Bar('Creating', max=options['number'])

        for i in range(options['number']):
            bar.next()
            try:
                article = ZenArticle.objects.create(
                    title=fake.bothify(text=f'Статья_{i} ????? ??? ????', letters=ru_letters),
                    link=fake.unique.url(),
                    likes=fake.pyint(min_value=0, max_value=9999999),
                    reads=fake.pyint(min_value=0, max_value=999999),
                    comments=fake.pyint(min_value=0, max_value=9999999),
                    to_parse_interval=fake.pyint(min_value=0, max_value=180*24*60*60),
                    public_date=fake.pyint(min_value=datetime.datetime(2021, 1, 1).timestamp(),
                                           max_value=datetime.datetime(2022, 1, 1).timestamp()),
                    public_time=fake.pyint(min_value=0, max_value=24*60*60),
                    length=fake.pyint(min_value=0, max_value=9999),
                    num_images=fake.pyint(min_value=0, max_value=999999),
                    audience=fake.pyint(min_value=0, max_value=9999999),
                    visitors=fake.pyint(min_value=0, max_value=999999),
                    read_time=fake.pyint(min_value=20, max_value=60*10),
                    subscribers=fake.pyint(min_value=0, max_value=9999999)
                )
                for j in range(10):
                    ZenFeed.objects.create(
                        article=article,
                        name=fake.bothify(text=f'Feed_{i}_{j}????? ????', letters=ru_letters),
                        users_num=fake.pyint(min_value=0, max_value=9999999)
                    )
            except IntegrityError:
                continue
        print('\n')
