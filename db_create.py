from project import db
from project.models import Task,User
from datetime import date

db.create_all()
db.session.commit()
