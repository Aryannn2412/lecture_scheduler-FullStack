from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models import Course, Instructor, Lecture, db
from forms import AddCourseForm, ScheduleLectureForm
from datetime import date

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Admin Dashboard
@admin_bp.route('/')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        return redirect(url_for('auth.login'))
    courses = Course.query.all()
    return render_template('admin_dashboard.html', courses=courses)

# Add Course
@admin_bp.route('/add-course', methods=['GET', 'POST'])
@login_required
def add_course():
    if current_user.role != 'admin':
        return redirect(url_for('auth.login'))

    form = AddCourseForm()
    if form.validate_on_submit():
        course = Course(
            name=form.name.data,
            level=form.level.data,
            description=form.description.data,
            image_url=form.image_url.data
        )
        db.session.add(course)
        db.session.commit()
        flash('✅ Course added successfully!', 'success')
        return redirect(url_for('admin.admin_dashboard'))

    return render_template('add_course.html', form=form)

# Schedule Lecture Page
@admin_bp.route('/schedule-lecture', methods=['GET', 'POST'])
@login_required
def schedule_lecture():
    if current_user.role != 'admin':
        return redirect(url_for('auth.login'))

    form = ScheduleLectureForm()

    # Populate select fields
    form.course.choices = [(c.id, c.name) for c in Course.query.all()]
    form.instructor.choices = [(i.id, i.name) for i in Instructor.query.filter_by(role='instructor').all()]

    if form.validate_on_submit():
        # ✅ Prevent duplicate date for same instructor
        existing_lecture = Lecture.query.filter_by(
            instructor_id=form.instructor.data,
            date=form.date.data
        ).first()

        if existing_lecture:
            flash('❌ This instructor already has a lecture scheduled on that date.', 'danger')
            return render_template('admin_schedule_lecture.html', form=form)

        # Create lecture
        lecture = Lecture(
            course_id=form.course.data,
            instructor_id=form.instructor.data,
            date=form.date.data
        )
        db.session.add(lecture)
        db.session.commit()
        flash('✅ Lecture scheduled successfully!', 'success')
        return redirect(url_for('admin.admin_dashboard'))

    return render_template('admin_schedule_lecture.html', form=form)
