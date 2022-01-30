import pytest

from zen.management.commands.settestdata import Command


@pytest.fixture
def set_test_data():
    def create(num):
        Command().handle(number=num)
    return create
