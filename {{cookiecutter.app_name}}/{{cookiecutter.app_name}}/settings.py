"""Application configuration."""
import os


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('{{cookiecutter.app_name | upper}}_SECRET', 'secret-key')
    APP_NAME = '{{cookiecutter.app_name}}'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    # Flask-Assects config
    ASSETS_DEBUG = False
    # Flask-DebugToolbar
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # Flask-babel config
    ACCEPT_LANGUAGES = ['es', 'en']
    BABEL_DEFAULT_LOCALE = 'es'
    # Flask-Cache config
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    # Flask-SQLAlchemy config
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Flask-User config
    USER_APP_NAME = APP_NAME
    USER_ENABLE_USERNAME = False
    USER_ENABLE_CHANGE_USERNAME = False
    USER_ENABLE_CONFIRM_EMAIL = False
    USER_ENABLE_FORGOT_PASSWORD = False
    USER_AFTER_LOGIN_ENDPOINT = 'user.profile'
    USER_PASSWORD_HASH = 'plaintext'
    USER_PASSWORD_SALT = os.environ.get('{{cookiecutter.app_name | upper}}_PASSWORD_SALT', 'password-salt')


class DevelopmentConfig(Config):
    """Development configuration."""

    ENV = 'development'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets


class TestingConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    WTF_CSRF_ENABLED = False  # Allows form testing


class ProductionConfig(Config):
    """Production configuration."""

    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('{{cookiecutter.app_name | upper}}_DATABASE_URL')
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    USER_PASSWORD_HASH = 'bcrypt'
    PREFERRED_URL_SCHEME = 'https'
