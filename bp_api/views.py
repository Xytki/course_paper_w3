from flask import Flask, Blueprint, jsonify
from werkzeug.exceptions import abort

from config import POST_PATH, COMMENTS_PATH
from posts.main.comment_main import CommentsDAO
from posts.main.post_main import PostDAO
from posts.main.post_model import PostModel
import logging

bp_api = Blueprint('bp_api', __name__)

posts_dao = PostDAO(POST_PATH)
comments_dao = CommentsDAO(COMMENTS_PATH)

api_logger = logging.getLogger("api_logger")


@bp_api.route('/posts/')
def api_posts_all():
    all_posts = posts_dao.get_all()
    api_logger.debug('All posts requested')
    return jsonify([post.as_dict() for post in all_posts]), 200


@bp_api.route('/posts/<int:pk>/')
def api_posts_single(pk):
    post = posts_dao.get_by_pk(pk)

    if post is None:
        api_logger.debug('Referring to a non-existent post')
        abort(404)
    api_logger.debug(f'Referring to post {pk}')
    return jsonify(post.as_dict()), 200


