from app import  db
from .models import Interview
from sqlalchemy import exc


class InterviewRepo():

    def fetch_all(self):
        return Interview.query.paginate(error_out=False)

    def filter_first(self, **kwargs):
        return Interview.query.filter_by(**kwargs).first()

    def create_Interview(self, candidate, interviewer, date, time, duration):

        interview = Interview(candidate=candidate, interviewer=interviewer, date=date, time=time, duration=duration)

        try:
            db.session.add(interview)
            db.session.commit()
            return interview
        except(exc.IntegrityError, exc.InvalidRequestError):
            db.session().rollback()