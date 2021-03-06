from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_moment import Moment
from flask_mail import Mail
from flask_login import LoginManager
from flask_wtf import CSRFProtect


db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
ckeditor = CKEditor()
bootstrap = Bootstrap()
mail = Mail()
login_manager = LoginManager()
csrf = CSRFProtect()

login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    from bluelog.models import Admin
    user = Admin.query.get(int(user_id))
    return user
