import flask_admin
import flask_admin.contrib.sqla
import flask_user

from .extensions import db
from .user.models import Role, User

class AdminLoginRequiredMixin(object):
    def is_accessible(self):
        return (
            False if (
                not flask_user.current_user.is_authenticated
                or not (flask_user.current_user.role and flask_user.current_user.role.name == 'admin')
                or not flask_user.current_user.active
                )
            else True)


class AdminModelView(AdminLoginRequiredMixin, flask_admin.contrib.sqla.ModelView):
    pass


class MyAdminIndexView(AdminLoginRequiredMixin, flask_admin.AdminIndexView):
    pass


def register_admin(app):
    admin = flask_admin.Admin(name='Admin', index_view=MyAdminIndexView(), template_mode='bootstrap3')
    admin.add_view(AdminModelView(Role, db.session))
    admin.add_view(AdminModelView(User, db.session))
    admin.init_app(app)
