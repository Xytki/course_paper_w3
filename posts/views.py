import logging

from flask import Flask, Blueprint, render_template, current_app, request
from werkzeug.exceptions import abort

from config import POST_PATH, COMMENTS_PATH
from posts.main.comment_main import CommentsDAO
from posts.main.post_main import PostDAO

posts = Blueprint('post_main', __name__, template_folder='templates')

posts_dao = PostDAO(POST_PATH)
comments_dao = CommentsDAO(COMMENTS_PATH)


@posts.route('/')
def index():
    all_posts = posts_dao.get_all()
    return render_template('index.html', posts=all_posts)


@posts.route('/posts/<int:pk>/')
def get_post_by_pk(pk):
    """Get a post by number"""
    post = posts_dao.get_by_pk(pk)
    comments = comments_dao.get_comments_by_post_id(pk)
    if post is None:
        abort(404)
    return render_template('post.html', post=post, comments=comments)


@posts.route('/users/<username>')
def get_posy_by_user(username):
    posts = posts_dao.get_posts_by_user(username)
    if not posts:
        abort(404, 'no such user')
    return render_template('user-feed.html', posts=posts)


@posts.route('/search/')
def search_page():
    search_query = request.args.get('s', '')
    if search_query == '':
        posts = []
    else:
        posts = posts_dao.search_for_posts(search_query)
    return render_template('search.html', posts=posts)
