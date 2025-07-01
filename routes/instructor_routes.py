from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from models import Lecture

instructor_bp = Blueprint('instructor', __name__, url_prefix='/instructor')

@instructor_bp.route('/')
@login_required
def instructor_dashboard():
    if current_user.role != 'instructor':
        return redirect(url_for('auth.login'))

    # Get all lectures assigned to this instructor
    lectures = Lecture.query.filter_by(instructor_id=current_user.id).order_by(Lecture.date.asc()).all()

    return render_template('instructor_dashboard.html', lectures=lectures)
