from app import app, db
from .models import Interview
from flask import request, jsonify
from dateutil import parser

# Endpoint to confirm that application is running
@app.route('/')
def index():
    return "Hello from database application!"


@app.route('/add-interview', methods=['POST'])
def interview_func():
    req_data = request.get_json()
    candidate = req_data['candidate']
    interviewer = req_data['interviewer']
    date = parser.parse(req_data['date'])
    time = parser.parse(req_data['time'])
    duration = req_data['duration']
    interview1 = Interview.query.filter_by(interviewer=interviewer, date=date, time=time).first()
    interview2 = Interview.query.filter_by(candidate=candidate, date=date, time=time).first()
    if interview1 is None and interview2 is None:
        try:
            t = Interview(candidate=candidate, interviewer=interviewer, date=date, time=time, duration=duration)
            db.session.add(t)
            db.session.commit()
            message = "Interview Successfully added"
            return jsonify(message), 201
        except Exception as e:
            return jsonify(message), 500
    else:
        message = "There is a conflicting interview"
        return jsonify(message), 400