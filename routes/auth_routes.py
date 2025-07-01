from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from models import Instructor, db
from forms import LoginForm, RegisterForm

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Instructor.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            if user.role == 'admin':
                return redirect(url_for('admin.admin_dashboard'))
            else:
                return redirect(url_for('instructor.instructor_dashboard'))
        else:
            flash(' Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = Instructor.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash(' Email already registered.', 'danger')
            return render_template('signup.html', form=form)

        user = Instructor(
            name=form.name.data,
            email=form.email.data,
            role=form.role.data  # ✅ Role from dropdown
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created! Please login.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
