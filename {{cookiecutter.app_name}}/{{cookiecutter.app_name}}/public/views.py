"""Public section, including homepage and signup."""
from flask import Blueprint, render_template, redirect, url_for

blueprint = Blueprint('public', __name__, static_folder='../static')


@blueprint.route('/')
def home():
    return redirect(url_for('user.login'))
