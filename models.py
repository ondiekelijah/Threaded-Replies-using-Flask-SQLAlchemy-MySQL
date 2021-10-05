from app import db ,migrate
from flask_sqlalchemy import event
from flask import current_app
import os
from datetime import datetime


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "<Post %r>" % self.title


class Comment(db.Model):
    comment_path_level_width = 6

    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    parent_id = db.Column(db.Integer, db.ForeignKey('comment.id'))

    author = db.Column(db.String(64))
    text = db.Column(db.Text())

    zpstring_id = db.Column(db.String(200), server_default='', index=True)
    thread_created_on = db.Column(db.DateTime, index=True)

    content_item_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    replies = db.relationship(
        'Comment', 
        backref=db.backref('parent', 
        remote_side=[id]),
        lazy='dynamic')





