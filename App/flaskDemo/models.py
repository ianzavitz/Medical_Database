from datetime import datetime
from flaskDemo import db, login_manager
from flask_login import UserMixin
from functools import partial
from sqlalchemy import orm

db.Model.metadata.reflect(db.engine)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    #id = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(20), unique=True, nullable=False)
    #email = db.Column(db.String(120), unique=True, nullable=False)
    #image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    #password = db.Column(db.String(60), nullable=False)
    #posts = db.relationship('Post', backref='author', lazy=True)
    __table__ = db.Model.metadata.tables['user']
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #title = db.Column(db.String(100), nullable=False)
    #date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #content = db.Column(db.Text, nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    __table__ = db.Model.metadata.tables['post']
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Hospital(db.Model):
    __table__ = db.Model.metadata.tables['hospital']
class Physician(db.Model):
    __table__ = db.Model.metadata.tables['physician']
class Patient(db.Model):
    __table__ = db.Model.metadata.tables['patient']
class Medical_Procedure(db.Model):
    __table__ = db.Model.metadata.tables['medical_procedure']
class Medical_Case(db.Model):
    __table__ = db.Model.metadata.tables['medical_case']
class Works_On(db.Model):
    __table__ = db.Model.metadata.tables['works_on']

# Hospital query facrory
def getHospital(columns=None):
    u = Hospital.query
    if columns:
        u = u.options(orm.load_only(*columns))
    return u

def getHospitalFactory(columns=None):
    return partial(getHospital, columns=columns)


# Physician query facrory
def getPhysician(columns=None):
    u = Physician.query
    if columns:
        u = u.options(orm.load_only(*columns))
    return u

def getPhysicianFactory(columns=None):
    return partial(getPhysician, columns=columns)


# Patient query facrory
def getPatient(columns=None):
    u = Patient.query
    if columns:
        u = u.options(orm.load_only(*columns))
    return u

def getPatientFactory(columns=None):
    return partial(getPatient, columns=columns)


# Medical_Procedure query facrory
def getMedical_Procedure(columns=None):
    u = Medical_Procedure.query
    if columns:
        u = u.options(orm.load_only(*columns))
    return u

def getMedical_ProcedureFactory(columns=None):
    return partial(getMedical_Procedure, columns=columns)


# Medical_Case query facrory
def getMedical_Case(columns=None):
    u = Medical_Case.query
    if columns:
        u = u.options(orm.load_only(*columns))
    return u

def getMedical_CaseFactory(columns=None):
    return partial(getMedical_Case, columns=columns)


# Works_On query facrory
def getWorks_On(columns=None):
    u = Works_On.query
    if columns:
        u = u.options(orm.load_only(*columns))
    return u

def getWorks_OnFactory(columns=None):
    return partial(getWorks_On, columns=columns)












    
