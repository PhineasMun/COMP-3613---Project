from App.models import Staff, Allocations
from App.database import db

def create_staff(name, email,role):
    newstaff = Staff(name=name, email=email, role=role)
    db.session.add(newstaff)
    db.session.commit()
    return newstaff


def view_staff(id):
    staff = Allocations.query.filter_by(course_id = id).all
    return staff