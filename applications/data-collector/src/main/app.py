from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Segments.sqlite3"

'''
Define the database model
used to store segments
'''
db = SQLAlchemy(app)
class Segment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    avg_grade = db.Column(db.Float, nullable=False)
    start_lat = db.Column(db.Float)
    start_long = db.Column(db.Float)
    end_lat = db.Column(db.Float)
    end_long = db.Column(db.Float)
    distance = db.Column(db.Float, nullable=False)

@app.route("/")
def main():
    db.create_all()
    # db.session.add(Segment(id=229781, name="Hawk Hill", avg_grade=5.7, start_lat=37.8331119, start_long=-122.4834356, end_lat=37.8280722, end_long=-122.4981393, distance=2684.8))
    # db.session.commit()
    segment = db.session.execute(db.select(Segment)).one()
    return "Segment: " + segment._asdict()['Segment'].name





