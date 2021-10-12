import os

import click
from flask import Flask, render_template

from .settings import config
from .extensions import db, migrate, moment, ckeditor, mail, bootstrap
from .blueprints.admin import admin_bp
from .blueprints.auth import auth_bp
from .blueprints.blog import blog_bp


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG_NAME', 'development')
    
    app = Flask('bluelog')
    app.config.from_object(config[config_name])

    register_logging(app)
    register_extensions(app)
    register_bluepirints(app)
    register_errors(app)
    register_shell_context(app)
    register_template_context(app)
    register_commands(app)

    return app

# 日志处理函数
def register_logging(app):
    pass


# 注册扩展函数
def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db=db)
    bootstrap.init_app(app)
    ckeditor.init_app(app)
    moment.init_app(app)
    mail.init_app(app)


# 注册蓝本函数
def register_bluepirints(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(blog_bp, prefix='/blog')


# 程序上下文处理函数
def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(
            db=db, 
            migrate=migrate, 
            bootstrap=bootstrap, 
            moment=moment,
            ckeditor=ckeditor,
            mail=mail
        )


# 模板上下文处理函数
def register_template_context(app):
    pass


# 错误处理函数
def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500


# 命令函数
def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        if drop:
            click.echo('This operation will delete the tables, doyou want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')