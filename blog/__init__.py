# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from os import path
# from flask_login import LoginManager

# db = SQLAlchemy()


# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'TOPsecretcadewgtrrjuuyjkimujadadadfagfagAGAGDFvafaFARFACSDVaferFasfFvaFVAf'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mc53hg:xau_YTFlUsuUiX79ccvVTVxNH6IQZOZUsIKb3@us-east-1.sql.xata.sh/static_blog:main?sslmode=require'
#     app.config['SECURITY_PASSWORD_SALT'] = "kjcfslijfcklsejfisjfisejfvilesjfivhsefuhseiflakjcflajdliajfcisjvkdmbkdjg8eutigfvniLIDJAFJSILVJ"
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.init_app(app)
#     app.instance_path = '/tmp'
#     UPLOAD_FOLDER = app.root_path+'tmp\\'+'static\\'
#     app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#     @app.errorhandler(404)
#     def no_match(e):
#         return render_template("404.html"), 404

#     from .views import views
#     from .auth import auth

#     app.register_blueprint(views, url_prefix='/')
#     app.register_blueprint(auth, url_prefix='/')

#     from .models import User

#     database(app)

#     login_manager = LoginManager()
#     login_manager.login_view = 'auth.login'
#     login_manager.login_message = "Please login first to use this page."
#     login_manager.login_message_category = "warning"
#     login_manager.init_app(app)

#     @login_manager.user_loader
#     def load_user(id):
#         return User.query.get(int(id))

#     return app


# def database(app):
#     if not path.exists('tmp/blog/database.sqlite3'):
#         with app.app_context():
#             db.create_all()


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TOPsecretcadewgtrrjuuyjkimujadadadfagfagAGAGDFvafaFARFACSDVaferFasfFvaFVAf'
    app.config['SECURITY_PASSWORD_SALT'] = "kjcfslijfcklsejfisjfisejfvilesjfivhsefuhseiflakjcflajdliajfcisjvkdmbkdjg8eutigfvniLIDJAFJSILVJ"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Use a writable directory for SQLite in Lambda
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.sqlite3'
    
    # Set instance path to /tmp to avoid write issues
    app.instance_path = '/tmp'
    UPLOAD_FOLDER = '/tmp/static/'  # Ensure uploads are stored in a writable location
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    db.init_app(app)

    @app.errorhandler(404)
    def no_match(e):
        return render_template("404.html"), 404

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    # Ensure the database is created if it doesn't exist
    database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = "Please login first to use this page."
    login_manager.login_message_category = "warning"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def database(app):
    db_path = '/tmp/database.sqlite3'  # Path within Lambda's writable directory
    if not path.exists(db_path):
        with app.app_context():
            db.create_all()
