import os
from flask import Flask
from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from dotenv import load_dotenv



db = SQLAlchemy()
migrate = Migrate()
load_dotenv()  # take environment variables from .env.



# Create a flask app method
def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

    db.init_app(app)
    migrate.init_app(app, db)


    class MyModelView(ModelView):
        def is_accessible(self):
            return True
        
    admin = Admin(app,name='Admin Panel', template_mode='bootstrap3')
    
    from models import Post,Comment
    
    admin.add_view(MyModelView(Post, db.session))
    admin.add_view(MyModelView(Comment, db.session))


    return app
