from flask import Blueprint, render_template, url_for, flash, redirect, session
from flask_login import current_user, login_user, logout_user
from flask_login.utils import login_required

from bluelog.forms import LoginForm
from bluelog.utils import redirect_back
from bluelog.models import Admin

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    for k, v in session.items():
        print('=====', k, v)
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.first()
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                flash('Welcome back.', 'info')
                return redirect_back()
            flash('Invalid username or password.', 'warning')
        else:
            flash('No account.', 'warning')
                        

    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successed.', 'info')
    return redirect_back()


@auth_bp.route('/settings')
@login_required
def settings():
    return render_template('admin/settings.html')