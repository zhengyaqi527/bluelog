
import click
from click.termui import prompt

from bluelog.fakes import fake_admin, fake_categories, fake_posts, fake_comments
from bluelog.extensions import db
from bluelog.models import Admin, Category


def register_commands(app):

    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create tables after drop.')
    def initdb(drop):
        if drop:
            click.confirm('This operation will delete all the tables, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')


    @app.cli.command()
    @click.option('--category', default=10, help='Quantity of categories, default is 10.')
    @click.option('--post', default=50, help='Quantity of posts, default is 50.')
    @click.option('--comment', default=500, help='Quantity of comments,default is 500.')
    def forge(category, post, comment):
        
        db.drop_all()
        db.create_all()
        
        click.echo('Generating the administrator...')
        fake_admin()

        click.echo('Generating %d categories...' % category )
        fake_categories(category)

        click.echo('Generating %d posts...' % post )
        fake_posts(post)

        click.echo('Generating %d comments...' % comment )
        fake_comments(comment)

        click.echo('Generating is done.')


    @app.cli.command()
    @click.option('--username', prompt=True, help='The username used to login.')
    @click.password_option('--password', prompt=True, help='The password used to login.')
    def init(username, password):
        
        admin = Admin.query.first()
        if admin:
            click.echo('The administrator alreader exists, updating...')
            admin.username = username
            admin.set_password(password)
        else:
            click.echo('Creating the tempory administrator account...')
            admin = Admin(
                username=username,
                blog_title='BLUELOG',
                blog_sub_title='The real blog.',
                name='Admin',
                about='This is my first blog.'
            )
            admin.set_password(password)
            db.session.add(admin)
        
        catefory = Category.query.first()
        if catefory is None:
            click.echo('Creating the default category...')
            catefory = Category(name='default')
            db.session.add(catefory)
        
        db.session.commit()
        click.echo('Done.')
