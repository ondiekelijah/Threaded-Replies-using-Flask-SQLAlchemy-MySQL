from wtforms import (
    StringField,
    TextAreaField,
)
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, EqualTo, Email, Regexp
from wtforms import ValidationError
from wtforms import validators


# No forms here

class CommentForm(FlaskForm):
    author = StringField(validators = [InputRequired()])
    comment = TextAreaField(validators = [InputRequired()])
class ReplyForm(FlaskForm):
    author = StringField(validators = [InputRequired()])
    reply = TextAreaField(validators = [InputRequired()])
