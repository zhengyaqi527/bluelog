
import click

from bluelog.fakes import fake_admin, fake_categories, fake_posts, fake_comments
from bluelog.extensions import db


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