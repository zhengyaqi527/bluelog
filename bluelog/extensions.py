from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_moment import Moment
from flask_mail import Mail


db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
ckeditor = CKEditor()
bootstrap = Bootstrap()
mail = Mail()
