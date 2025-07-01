from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match.')
    ])
    role = SelectField('Register As', choices=[
        ('instructor', 'Instructor'),
        ('admin', 'Admin')
    ], validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class AddCourseForm(FlaskForm):
    name = StringField('Course Name', validators=[DataRequired()])
    level = SelectField('Level', choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ])
    description = TextAreaField('Description')
    image_url = StringField('Image URL (optional)')
    submit = SubmitField('Add Course')

class ScheduleLectureForm(FlaskForm):
    course = SelectField('Select Course', coerce=int, validators=[DataRequired()])
    instructor = SelectField('Select Instructor', coerce=int, validators=[DataRequired()])
    date = DateField('Lecture Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Schedule Lecture')
