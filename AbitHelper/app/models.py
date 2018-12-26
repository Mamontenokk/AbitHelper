from app import db

class Speciality(db.Model):
	__tablename__ = 'Specialities'
	id = db.Column('id', db.Integer, primary_key=True)
	university = db.Column('university', db.String(120), index=True)
	faculty = db.Column('Faculty', db.String(120), index=True)