import os
from dotenv import load_dotenv
from flask import Flask, request

from app.database.db import initialize_db
from app.routes.users import users_bp
from app.routes.jobs import jobs_bp
from app.routes.vendors import vendors_bp
from app.routes.generalcontractors import generalcontractors_bp
from app.routes.buildings import buildings_bp
from app.routes.deliveries import deliveries_bp

# this will generate a path to this file (<os abs path>/job_tracker_api/app), we use replace to get the project root
# HACK! we should clean this up ^^^^
basedir = os.path.abspath(os.path.dirname(__file__)).replace('/app', '')
env_path = os.path.join(basedir, '.env')
load_dotenv(env_path)

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['MONGODB_SETTINGS'] = {
        'host': os.environ.get('MONGODB_HOST', 'mongodb://127.0.0.1/job_tracker'),
        # the username and password will be required for staging and prod environments
        # 'username': os.environ.get('MONGODB_USERNAME', ''),
        # 'password': os.environ.get('MONGODB_PASSWORD', ''),
    }
    
    # initialize mongo db
    initialize_db(app)
    
    # register app routes
    app.register_blueprint(users_bp)
    app.register_blueprint(jobs_bp)
    app.register_blueprint(vendors_bp)
    app.register_blueprint(generalcontractors_bp)
    app.register_blueprint(buildings_bp)
    app.register_blueprint(deliveries_bp)

    # a simple page that says hellos
    @app.route('/')
    def noPath():
        return 'Hello, no path!!!!!!'

    return app

