from App.models import Course, Staff, Allocation
from App.database import db

def create_course(name, description):
    newcourse = Course(name=name, description=description)
    db.session.add(newcourse)
    db.session.commit()
    return newcourse

def allocate_staff(cid,sid):
    course = Allocation.query.filter_by(Allocation.courseid==cid, Staff.id==sid).first

    return course

'''def add_staff(id):
    try:
        s'''
