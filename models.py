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
    _N = 6

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
    author = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
    path = db.Column(db.Text, index=True)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    parent_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    
    replies = db.relationship(
        'Comment', backref=db.backref('parent', remote_side=[id]),
        lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()
        prefix = self.parent.path + '.' if self.parent else ''
        self.path = prefix + '{:0{}d}'.format(self.id, self._N)
        db.session.commit()

    def level(self):
        return len(self.path) // self._N - 1



