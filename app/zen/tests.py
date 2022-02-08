from django.test import Client
import pytest

from zen.models import ZenArticle, ZenFeed


class TestZenArticleBulkView:
    """"""

    @pytest.mark.django_db
    def test_pagination(self, set_test_data):
        """test pagination params page and size (default size = 5, page = 0)"""
        set_test_data(10)
        c = Client()
        response = c.get('/zen_articles/?page=1&size=10')
        assert response.data['last_page'] == 1
        response = c.get('/zen_articles/?page=1&size=5')
        assert response.data['last_page'] == 2

    @pytest.mark.django_db
    def test_filters(self, set_test_data):
        """"""
        set_test_data(10)
        c = Client()
        response = c.get('/zen_articles/?title=Статья_0')
        assert len(response.data['data']) == 1
        response = c.get('/zen_articles/?title=Статья_10')
        assert len(response.data['data']) == 0
        response = c.get('/zen_articles/?title=')
        assert len(response.data['data']) == 5

        response = c.get('/zen_articles/?likes=9,11&reads=99,101')
        assert len(response.data['data']) == 1
        response = c.get('/zen_articles/?likes=0,40')
        assert len(response.data['data']) == 5

    @pytest.mark.django_db
    def test_auth_user(self, create_user, set_test_data):
        """"""

        user, token = create_user()
        set_test_data(1)
        c = Client()
        response = c.get('/zen_articles/', HTTP_AUTHORIZATION=f'Token {token}')
        assert set(response.data['data'][0].keys()) == {
            'id', 'title', 'link', 'likes', 'reads', 'comments', 'length',
            'num_images', 'visitors', 'read_time', 'to_parse_interval',
            'public_datetime', 'audience', 'subscribers', 'feeds'
        }
        assert set(response.data['data'][0]['feeds'][0].keys()) == {'id', 'name', 'users_num'}

    @pytest.mark.django_db
    def test_not_auth_user(self, create_user, set_test_data):
        """"""
        set_test_data(1)
        c = Client()
        response = c.get('/zen_articles/')
        assert set(response.data['data'][0].keys()) == {
            'title', 'link', 'likes', 'reads', 'comments', 'length', 'num_images', 'visitors', 'read_time'}

    @pytest.mark.django_db
    def test_valid_post_request(self, create_user):
        """"""
        user, token = create_user(is_staff=True)
        c = Client()
        valid_dict = {
            'title': 'title',
            'link': 'http://link.com',
            'likes': 0,
            'reads': 1,
            'comments': 2,
            'to_parse_interval': 3,
            'public_datetime': 4,
            'length': 5,
            'num_images': 6,
            'audience': 7,
            'visitors': 8,
            'read_time': 9,
            'subscribers': 10,
            'feeds': [
                {
                    'name': 'feed1',
                    'users_num': 1
                },
                {
                    'name': 'feed2',
                    'users_num': 2
                },
                {
                    'name': 'feed3',
                    'users_num': 3
                }
            ]
        }
        response = c.post('/zen_articles/', valid_dict, content_type='application/json', HTTP_AUTHORIZATION=f'Token {token}')
        assert response.status_code == 201
        assert ZenArticle.objects.count() == 1
        assert ZenFeed.objects.count() == 3

    @pytest.mark.django_db
    def test_invalid_post_request(self, create_user):
        """"""
        user, token = create_user(is_staff=True)
        c = Client()
        dict = {}
        response = c.post('/zen_articles/', dict, content_type='application/json', HTTP_AUTHORIZATION=f'Token {token}')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_auth_post_request(self, create_user):
        """"""
        user, token = create_user()
        c = Client()
        dict = {}
        response = c.post('/zen_articles/', dict, content_type='application/json')
        assert response.status_code == 401

        response = c.post('/zen_articles/', dict, content_type='application/json', HTTP_AUTHORIZATION=f'Token {token}')
        assert response.status_code == 403
