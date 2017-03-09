"""User models."""
import datetime as dt

from flask import current_app
from flask_user import UserMixin

from {{cookiecutter.app_name}}.database import Model, db, reference_col


class Role(Model):
    """A role for a user."""

    __tablename__ = 'roles'
    name = db.Column(db.String(80), unique=True, nullable=False)
    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Role({name})>'.format(name=self.name)


class User(UserMixin, Model):
    """A user of the app."""

    __tablename__ = 'users'
    email = db.Column(db.Unicode(255), unique=True, nullable=False)
    #: The hashed password
    password = db.Column(db.String(255), nullable=True)
    reset_password_token = db.Column(db.String(100), nullable=False, default='')
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    active = db.Column(db.Boolean(), default=False)
    role_id = reference_col('roles', nullable=True)
    role = db.relationship('Role', backref='users')

    def __init__(self, email, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        with current_app.app_context():
            self.password = current_app.user_manager.generate_password_hash(password)

    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({email!r})>'.format(email=self.email)
