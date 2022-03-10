from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

class LoginForm(FlaskForm):
  username = StringField('Username')
  password = PasswordField('Password')
  submit = SubmitField('Sign In')

class SignupForm(FlaskForm):
  username = StringField('Username')
  password = PasswordField('Password')
  submit = SubmitField('Sign Up')