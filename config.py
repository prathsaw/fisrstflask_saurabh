class Config(object):
    #common configruation
    
    #Put any configuration here that are common across all environments
    SECRET_KEY='zxckddscbdjksf123'

    SQLALCHEMY_DATABASE_URI="mysql://root:saurabh21@localhost/mydbase"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopmentConfig(Config):

    DEBUG=True
    SQLALCHEMY_ECHO=True


class TestingConfig(Config):
    #testing configuration

    DEBUG=True
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI="mysql://root:saurabh21@localhost/flasktest"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProductionConfig(Config):
    DEBUG=False


app_config={
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig
}


# development=DevelopmentConfig()
# testing=TestingConfig()
# production=ProductionConfig()