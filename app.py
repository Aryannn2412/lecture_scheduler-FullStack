import os
from flask import Flask, redirect, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from models import db, Instructor

# Initialize Login Manager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    # SQLAlchemy 2.0 compliant user loader
    return db.session.get(Instructor, int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register Blueprints
    from routes.admin_routes import admin_bp
    from routes.instructor_routes import instructor_bp
    from routes.auth_routes import auth_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(instructor_bp)
    app.register_blueprint(auth_bp)

    # Default route redirect to login
    @app.route('/')
    def home():
        return redirect(url_for('auth.login'))

    # CLI command to create DB
    @app.cli.command('create-db')
    def create_db():
        with app.app_context():
            db.create_all()
            print("✅ Database tables created.")

    return app

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # default 10000 for Render
    app.run(host='0.0.0.0', port=port, debug=True)

