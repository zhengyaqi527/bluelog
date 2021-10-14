from flask import Blueprint, render_template

from bluelog.forms import LoginForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
def logout():
    return 'logout'