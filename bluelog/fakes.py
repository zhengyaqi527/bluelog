import random

from faker import Faker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import session

from bluelog.models import Admin, Category, Comment, Post
from bluelog.extensions import db

fake = Faker()

def fake_admin():
    admin = Admin(
        username='admin',
        blog_title='Blueblog',
        blog_sub_title='The real blog.',
        name='Mima Kirigoe',
        about='This is my first blog.'
    )
    db.session.add(admin)
    db.session.commit()


def fake_categories(count=10):
    category = Category(name='default')
    db.session.add(category)

    for i in range(count):
        category = Category(name=fake.word())
        db.session.add(category)

        # 避免发生category重名异常
        try:
            db.session.commit()
        except IntegrityError():
            db.session.rollback()


def fake_posts(count=50):
    for i in range(50):
        post = Post(
            title=fake.sentence(3),
            body=fake.text(2000),
            category=Category.query.get(random.randint(1, Category.query.count()))
        )
        db.session.add(post)
    
    db.session.commit()


def fake_comments(count=500):
    for i in range(count):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

    salt = int(count * 0.1)
    # 未审核comment
    for i in range(salt):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=False,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

    # 管理员发布的comment
    for i in range(salt):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            from_admin=True,
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

    db.session.commit()

    # replies
    for i in range(salt):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count())),
            replied=Comment.query.get(random.randint(1, Comment.query.count()))
        )
        db.session.add(comment)
    db.session.commit()