import os

from flask import Flask, request
# from flask_mongoengine import MongoEngine

from app.database.jobs_db import initialize_jobs_db
from app.routes.jobs import jobs_bp

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping()
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    initialize_db(app)
    app.register_blueprint(jobs_bp)
    # a simple page that says hello
    @app.route('/')
    def noPath():
        return 'Hello, no path!!!!!!'

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

