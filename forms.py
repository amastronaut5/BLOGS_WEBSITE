from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Email, Length, Regexp,EqualTo
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Create a form to register new users
# class RegisterForm(FlaskForm):
#     email = StringField("Email", validators=[DataRequired(), Email(message="Invalid email address. Please enter a valid email.")])
#     password = PasswordField("Password", validators=[DataRequired(),Length(min=8, message="Password must be at least 8 characters."),
#         Regexp(
#             regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
#             message="Password must contain at least one uppercase letter, one number, and one special character."
#         )])
#     name = StringField("Name", validators=[DataRequired()])
#     submit = SubmitField("Sign Me Up!")


class RegisterForm(FlaskForm):
    email = EmailField("Email",
                       validators=[
            DataRequired(message="Email is required."),
            Email(message="Invalid email address. Please enter a valid email.")])
    name = StringField(
        "Name",
        validators=[DataRequired(message="Name is required.")])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required."),
            Length(min=8, message="Password must be at least 8 characters."),
            Regexp(
                regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
                message="Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character."
            )
        ]
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(message="Please confirm your password."),
            EqualTo('password', message="Passwords must match.")
        ]
    )
    
    submit = SubmitField("Sign Me Up!")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(message="Invalid email address. Please enter a valid email.")])
    password = PasswordField("Password", validators=[DataRequired(),])
    submit = SubmitField("Let Me In!")


# Create a form to add comments
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
