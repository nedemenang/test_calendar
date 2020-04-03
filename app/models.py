from app import db


class Interview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidate = db.Column(db.String(64))
    interviewer = db.Column(db.String(64))
    date = db.Column(db.DateTime)
    time = db.Column(db.DateTime)
    duration = db.Column(db.Integer)

