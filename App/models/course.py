# from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Course(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    description = db.Column(db.String(300) )

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
      return f'<User {self.id} {self.name} - {self.description}>'
    
    # def create_course(self, id, text)
    