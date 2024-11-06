from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired, Email

class NamerForm(FlaskForm):
    first_name = StringField("Enter your first name :", validators= [DataRequired()])
    last_name = StringField("Enter your last name :", validators= [DataRequired()])
    email_address = StringField("Enter your email address :", validators= [Email(), DataRequired()])
    
    submit = SubmitField("Book")

class LoginForm(FlaskForm):
    email_address = StringField("Email address :", validators= [Email(), DataRequired()])
    password = PasswordField("Password :", validators= [DataRequired()])
    
    submit = SubmitField("Login")