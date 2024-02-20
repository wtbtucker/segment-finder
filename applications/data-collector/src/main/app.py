from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Segments.sqlite3"

db = SQLAlchemy(app)
from SegmentRecord import Segment

def get_segment() -> Segment:
    return db.session.execute(db.select(Segment)).one()

@app.route("/")
def main():
    db.create_all()
    # db.session.add(Segment(id=229781, name="Hawk Hill", avg_grade=5.7, start_lat=37.8331119, start_long=-122.4834356, end_lat=37.8280722, end_long=-122.4981393, distance=2684.8))
    # db.session.commit()
    segment = get_segment()
    return "Segment: " + segment._asdict()['Segment'].name





