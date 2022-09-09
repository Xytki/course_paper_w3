import os

POST_PATH = os.path.join('data', 'posts.json')
COMMENTS_PATH = os.path.join('data', 'comments.json')

LOGGER_API_PATH = os.path.join('logs', 'api.log')
LOGGER_FORMAT = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s)"