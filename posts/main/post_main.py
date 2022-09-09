import json
from json import JSONDecodeError

from posts.main.post_model import PostModel


class PostDAO:
    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """Method loading data"""
        try:
            with open(self.path, encoding='utf-8') as file:
                post_data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            raise f'Не удается получить данные из файла {self.path}'

        instances = [PostModel(**post_data) for post_data in post_data]
        return instances

    def get_all(self):
        """Returns all posts"""
        data = self._load_data()
        return data

    def get_by_pk(self, pk):
        """The returned pk sample, if there is one"""
        if type(pk) != int:
            raise TypeError('pk must be an int')
        _all_posts = self.get_all()
        for post in _all_posts:
            if post.pk == pk:
                return post

    def get_posts_by_user(self, user_name):
        """The returned sample authors"""
        user_name = user_name.lower()
        all_posts_ = self.get_all()
        matching_posts = [post for post in all_posts_ if post.poster_name.lower() == user_name]
        return matching_posts

    def search_for_posts(self, query):
        """The returned sample post = query"""
        query = str(query)
        posts = self.get_all()
        matching_posts = [post for post in posts if query.lower() in post.content.lower()]
        return matching_posts
