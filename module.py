# coding=utf-8
# @File  : module.py
# @Author: PuJi
# @Date  : 3/23/18

from flask_sqlalchemy import SQLAlchemy
from blog import app
# from src import wallet


db = SQLAlchemy(app)


class User(db.Model):
    """Represents Protected users."""

    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    # Establish contact with Post's ForeignKey: user_id
    posts = db.relationship(
        'Post',
        backref='users',
        lazy='dynamic'
    )

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User '{}'>".format(self.username)


class Comment(db.Model):
    """Represents Protected comments."""


    __tablename__ = 'comments'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Model Comment "{}>'.format(self.name)


posts_tags = db.Table('posts_tags',
                      db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
                      db.Column('tag_id', db.String(45), db.ForeignKey('tags.id'))
                      )


class Post(db.Model):
    """Represents Protected posts."""

    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    # set the foreign key for Post
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))
    # Establish contact with Comment's ForeignKey: post_id
    comments = db.relationship(
        'Comment',
        backref='posts',
        lazy='dynamic'
    )
    # many to many:posts <==> tags
    tags = db.relationship(
        'Tag',
        secondary=posts_tags,
        backref=db.backref('posts', lazy='dynamic')
    )

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Model Post '{}'>".format(self.title)


class Tag(db.Model):
    """Represents Protected tags."""


    __tablename__ = 'tags'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Model Tag '{}'>".format(self.name)







