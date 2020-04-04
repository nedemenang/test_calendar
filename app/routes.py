from app import app
from flask import request, jsonify
from dateutil import parser
from .repo import InterviewRepo


interview_repo = InterviewRepo()

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
    interview1 = interview_repo.filter_first(interviewer=interviewer, date=date, time=time)
    interview2 = interview_repo.filter_first(candidate=candidate, date=date, time=time)
    if interview1 is None and interview2 is None:
        try:
            interview = interview_repo.create_Interview(candidate=candidate, interviewer=interviewer, date=date, time=time, duration=duration)
            if interview:
                message = "Interview Successfully added"
                return jsonify(message), 201
        except Exception as e:
            return jsonify(message), 500
    else:
        message = "There is a conflicting interview"
        return jsonify(message), 400


@app.route('/get-interview', methods=['GET'])
def interview_list_func():
    interviews = interview_repo.fetch_all()
    interview_list = [interview.serialize() for interview in interviews.items]
    return jsonify(interview_list), 201