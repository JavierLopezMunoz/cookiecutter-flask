"""Create an application instance."""
from flask.helpers import get_debug_flag

from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.settings import DevelopmentConfig, ProductionConfig


application = create_app(DevelopmentConfig if get_debug_flag() else ProductionConfig)
