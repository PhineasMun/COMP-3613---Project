# from sqlalchemy.sql.expression import func 
# from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Allocations(db.Model):
  __tablename__ ='allocations'
  id = db.Column(db.String, primary_key=True)
  course_id = db.Column(db.String, db.ForeignKey('course.id'), nullable=False)
  staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
#   last_modified = db.Column(db.DateTime, default=func.now(), onupdate=func.now())

def __repr__(self):
    return f'<Allocations {self.id} >'