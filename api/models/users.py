from ..utils import db

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password_hash = db.Column(db.String(128), nullable=False)
	is_admin = db.Column(db.Boolean, default=False)
	is_active = db.Column(db.Boolean, default=False)
	requests = db.relationship('Request', backref='user', lazy=True)

	def __repr__(self):
		return f"<User {self.username}>"