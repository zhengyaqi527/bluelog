import os

dev_db = 'postgresql://zhengyaqi@localhost/bluelog'
test_db = 'postgresql://zhengyaqi@localhost/bluelog'
prod_db = 'postgresql://zhengyaqi@localhost/bluelog'

class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', test_db)

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', prod_db)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}