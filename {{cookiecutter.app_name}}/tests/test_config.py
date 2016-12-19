# -*- coding: utf-8 -*-
"""Test configs."""
from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.settings import DevelopmentConfig, ProductionConfig


def test_production_config():
    """Production config."""
    app = create_app(ProductionConfig)
    assert app.config['ENV'] == 'production'
    assert app.config['DEBUG'] is False
    assert app.config['DEBUG_TB_ENABLED'] is False
    assert app.config['ASSETS_DEBUG'] is False


def test_dev_config():
    """Development config."""
    app = create_app(DevelopmentConfig)
    assert app.config['ENV'] == 'development'
    assert app.config['DEBUG'] is True
    assert app.config['ASSETS_DEBUG'] is True
