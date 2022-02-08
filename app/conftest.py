import pytest
from django.contrib.auth.models import User

from django.core.management import call_command
from rest_framework.authtoken.models import Token


@pytest.fixture
def set_test_data():
    def set_data(num):
        call_command('settestdata', number=num)
    return set_data


@pytest.fixture
def create_user():
    def create(**kwargs):
        user = User.objects.create_user(username='test_user', password='test', **kwargs)
        token = Token.objects.create(user=user)
        return user, token
    return create
