from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from constants import SecretsManager

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20,message="Name should be more than 2 characters and less than 20 characters")])
    email = StringField('Email',validators=[DataRequired(),Email('not a valid email')])
    password = PasswordField('Password',validators=[DataRequired(),Regexp(SecretsManager.PASSWORD_REGEX.value,message='Invalid Password. Password must contain minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo("password","Passwords don't match")])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Regexp(SecretsManager.PASSWORD_REGEX.value,message='Invalid Password. Password must contain minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
