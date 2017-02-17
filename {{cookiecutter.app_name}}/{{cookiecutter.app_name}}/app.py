"""The app module, containing the app factory function."""
import flask

from {{cookiecutter.app_name}} import commands, public, user
from {{cookiecutter.app_name}}.admin import register_admin
from {{cookiecutter.app_name}}.assets import assets
from {{cookiecutter.app_name}}.extensions import babel, cache, csrf_protect, db, debug_toolbar, migrate
from {{cookiecutter.app_name}}.settings import ProductionConfig


def create_app(config_object=ProductionConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = flask.Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_admin(app)
    register_commands(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    assets.init_app(app)
    babel.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    from flask_user import UserManager, SQLAlchemyAdapter
    from .user.models import User
    user_manager = UserManager(SQLAlchemyAdapter(db, User))
    user_manager.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public.views.blueprint)
    return None


def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return flask.render_template('{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


def register_shellcontext(app):
    """Register shell context objects."""
    def shell_context():
        """Shell context objects."""
        return {
            'db': db,
            'User': user.models.User}

    app.shell_context_processor(shell_context)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)
    app.cli.add_command(commands.create_admin_user, 'create-admin-user')
