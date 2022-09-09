import main
import pytest
import os


class TestApi:
    post_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
    parametrize = [1, 3, 5]

    @pytest.fixture
    def app_fix(self):
        app = main.app
        app.config['DATA_PATH_POST'] = os.path.join('data', 'posts.json')
        test_client = app.test_client()
        return test_client

    @pytest.mark.parametrize("pk", parametrize)
    def test_single_post_has_correct_data(self, app_fix, pk):
        result = app_fix.get(f"/api/posts/{pk}", follow_redirects=True)
        post = result.get_json()
        assert post['pk'] == pk

    def test_all_posts(self, app_fix):
        result = app_fix.get("/api/posts", follow_redirects=True)
        assert result.status_code == 200

    def test_404(self, app_fix):
        result = app_fix.get("/api/posts/0", follow_redirects=True)
        assert result.status_code == 404

    def test_keys(self, app_fix):
        result = app_fix.get('/api/posts/1', follow_redirects=True)
        post = result.get_json()
        assert post.keys() == self.post_keys


