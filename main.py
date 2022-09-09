from flask import Flask, render_template
from bp_api.views import bp_api
from posts.views import posts
import conf_log


def the_greate_app(config_path):
    app = Flask(__name__)
    app.register_blueprint(posts)
    app.register_blueprint(bp_api, url_prefix='/api')
    app.config.from_pyfile(config_path)
    conf_log.config(app)
    return app


app = the_greate_app('config.py')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()

