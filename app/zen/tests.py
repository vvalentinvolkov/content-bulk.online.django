from django.test import Client
import pytest


@pytest.mark.django_db
def test_zen_article_bulk_view(set_test_data):
    set_test_data(10)
    c = Client()
    response = c.get('/zen_articles/?page=1&size=10')
    assert response.data['last_page'] == 1
    response = c.get('/zen_articles/?page=1&size=5')
    assert response.data['last_page'] == 2


@pytest.mark.django_db
def test_zen_article_bulk_view(set_test_data):
    set_test_data(10)
    c = Client()
    response = c.get('/zen_articles/?page=1&size=10')
    assert response.data['last_page'] == 1
