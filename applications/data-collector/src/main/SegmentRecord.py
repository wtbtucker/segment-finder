from app import db

'''
Define the database model
used to store segments
'''
class Segment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    avg_grade = db.Column(db.Float, nullable=False)
    start_lat = db.Column(db.Float)
    start_long = db.Column(db.Float)
    end_lat = db.Column(db.Float)
    end_long = db.Column(db.Float)
    distance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return self.name