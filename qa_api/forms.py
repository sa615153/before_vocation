from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from .models import Machine, MajorTask, SubTask, SubtaskNameProperty
from wtforms.validators import DataRequired, length, Regexp, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class UserAddTaskForm(Form):
    gitDir = StringField(u'gitDir', validators=[DataRequired(), length(4,50)])
    submit = SubmitField(u'submit')

class UserLoginForm(Form):
    userName = StringField(u'username', validators=[DataRequired(), length(4.50)])
    passWord = PasswordField(u'password', validators= [DataRequired()])


