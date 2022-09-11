import pytest

import main
from posts.main.post_main import PostDAO

keys_should_be = fields = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


class TestMain:

    @pytest.fixture()
    def app_fix(self):
        app = main.app
        test_client = app.test_client()
        return test_client

    @pytest.fixture
    def post_main(self):
        post_main_instance = PostDAO('data/posts.json')
        return post_main_instance

    def test_root_status(self, app_fix):
        response = app_fix.get('/', follow_redirects=True)
        assert response.status_code == 200, "Status code is incorrect"

    def test_get_html(self, post_main):
        response = post_main.get_all()
        assert type(response) == list, 'Incorrect type for result'

    def test_get_pk(self, post_main):
        response = post_main.get_by_pk(1)
        assert response.pk == 1, 'Incorrect number'

    def test_get_pk_none(self, post_main):
        post = post_main.get_by_pk(0)
        assert post is None, 'Should be None for not existing pk'



