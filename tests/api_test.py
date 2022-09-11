import main
import pytest
import os


class TestApi:
    post_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
    parametrize = [1, 3, 5]

    @pytest.fixture()
    def api_fix(self):
        app = main.app
        app.config['DATA_PATH_POST'] = os.path.join('data', 'posts.json')
        test_client = app.test_client()
        return test_client

    def test_all_posts(self, api_fix):
        results = api_fix.get("/api/posts", follow_redirects=True)
        assert results.status_code == 200, "Status code is incorrect"

    def test_404(self, api_fix):
        result = api_fix.get("/api/posts/0", follow_redirects=True)
        assert result.status_code == 404, "No information found"

    def test_keys(self, api_fix):
        result = api_fix.get('/api/posts/1', follow_redirects=True)
        post = result.get_json()
        assert post.keys() == self.post_keys

    @pytest.mark.parametrize("pk", parametrize)
    def test_single_post_has_correct_data(self, api_fix, pk):
        result = api_fix.get(f"/api/posts/{pk}", follow_redirects=True)
        post = result.get_json()
        assert post['pk'] == pk

