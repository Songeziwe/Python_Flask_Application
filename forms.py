from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

class LoginForm(FlaskForm):
  username = StringField('Username')

  submit = SubmitField('Login')

class SignupForm(FlaskForm):
  username = StringField('Username')
  password = PasswordField('Password')
  submit = SubmitField('Login')