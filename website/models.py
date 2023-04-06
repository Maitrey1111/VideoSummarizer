from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique = True)
    name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    
class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)