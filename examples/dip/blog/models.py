from navycut.orm import db


# print (current_app.config)

# create your models here: 

#demo models
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    subject = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class Gargi(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    subject = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class Aniket(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    subject = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(), nullable=False)
    is_active = db.Column(db.Boolean, default=True)