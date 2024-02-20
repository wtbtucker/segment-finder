from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Segments.sqlite3"

db = SQLAlchemy(app)
from SegmentRecord import Segment
from SegmentDataGateway import SegmentDataGateway
from StravaDataGateway import StravaDataGateway


@app.route("/")
def main():
    db.create_all()
    # db.session.add(Segment(id=229781, name="Hawk Hill", avg_grade=5.7, start_lat=37.8331119, start_long=-122.4834356, end_lat=37.8280722, end_long=-122.4981393, distance=2684.8))
    # db.session.commit()
    stravaGateway = StravaDataGateway()
    segments = stravaGateway.get_starred_segments()
    print(segments)
    gateway = SegmentDataGateway()
    segment = gateway.get_segment(229781)
    return "Segment: " + segment._asdict()['Segment'].name





