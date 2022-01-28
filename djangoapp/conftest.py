import datetime

import pytest
from django.db import IntegrityError
from faker import Faker

from zen.models import ZenArticle, ZenFeed


@pytest.fixture
def set_test_data():
    fake = Faker()
    ru_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    def create(num):
        for i in range(num):
            try:
                article = ZenArticle.objects.create(
                    title=fake.bothify(text='Статья ??????? ????? ???????? ???? ????', letters=ru_letters),
                    link=fake.unique.url(),
                    likes=fake.pyint(min_value=0, max_value=9999999),
                    reads=fake.pyint(min_value=0, max_value=9999999),
                    comments=fake.pyint(min_value=0, max_value=9999999),
                    to_parse_interval=fake.time_delta(end_datetime=datetime.timedelta(days=300)),
                    public_date=fake.date_between(start_date=datetime.date(year=2021, month=1, day=1)),
                    public_time=fake.date_time().time(),
                    length=fake.pyint(min_value=0, max_value=9999999),
                    num_images=fake.pyint(min_value=0, max_value=9999999),
                    audience=fake.pyint(min_value=0, max_value=9999999),
                    visitors=fake.pyint(min_value=0, max_value=9999999),
                    read_time=fake.time_delta(end_datetime=datetime.timedelta(hours=2)),
                    subscribers=fake.pyint(min_value=0, max_value=9999999)
                )
                for _ in range(3):
                    ZenFeed.objects.create(
                        article=article,
                        name=fake.bothify(text='????? ???????', letters=ru_letters),
                        users_num=fake.pyint(min_value=0, max_value=9999999)
                    )
            except IntegrityError:
                continue
    return create
