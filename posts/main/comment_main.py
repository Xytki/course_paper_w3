import json
from json import JSONDecodeError
from posts.main.post_comment import CommentModel


class CommentsDAO:
    def __init__(self, path):
        self.path = path

    def load_comments(self):
        try:
            with open(self.path, encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise f'Unable to get data from file {self.path}'
        instances = [CommentModel(**data) for data in data]
        return instances

    def get_all_comments(self):
        """Returns all comments"""
        data_comments = self.load_comments()
        return data_comments

    def get_comments_by_post_id(self, post_id):
        """Returns comments of a specific post"""
        comments = self.load_comments()
        comments_match = [comment for comment in comments if comment.post_id == post_id]
        return comments_match

