from project import create_app, db
from project.models.User import User
from project.models.Therapist import Therapist
from project.models.Admin import Admin


app = create_app()

with app.app_context():
    db.create_all()
