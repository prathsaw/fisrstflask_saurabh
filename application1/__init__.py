from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config



db=SQLAlchemy()

def create_app(config_name):
    
    app=Flask(__name__)
    app.config.from_object(app_config[config_name])
    from application1.details.views import mod
    db.init_app(app)
    app.register_blueprint(mod)
    
    return app


# def create_app(app_config):
#     from application1.users.views import mod
#     app=Flask(__name__)

#     app.register_blueprint(mod)
    
#     return app