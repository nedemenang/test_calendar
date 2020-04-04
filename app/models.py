from app import db


class Interview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidate = db.Column(db.String(64))
    interviewer = db.Column(db.String(64))
    date = db.Column(db.DateTime)
    time = db.Column(db.DateTime)
    duration = db.Column(db.Integer)

    def serialize(self):
        s = {to_camel_case(column.name): getattr(self, column.name) for column in self.__table__.columns}

        return s


def to_camel_case(snake_str):
    title_str = snake_str.title().replace("_", "")
    return title_str[0].lower() + title_str[1:]

