# from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Staff(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    role = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(300), nullable=False )

def __init__(self, name, email,role):
    self.name = name
    self.email = email
    self.role = role

def __repr__(self):
      return f'<User {self.id} {self.name} - {self.email} - {self.role}>'


  