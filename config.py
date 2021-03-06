import os


class Config(object):
    DEBUG = os.getenv("DEBUG", False)
    TESTING = False
    PORT = os.getenv("PORT", 8080)
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")

    SANIC_APP_URL = os.getenv("SANIC_APP_URL", "http://basic-sanic-app:8000")

    SECRET_KEY = os.getenv('SECRET_KEY', 'test')


class DevelopmentConfig(Config):
    DEBUG = os.getenv("DEBUG", True)
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "DEBUG")


class TestingConfig(DevelopmentConfig):
    DEBUG = False
    TESTING = True
