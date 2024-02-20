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
    stravaGateway = StravaDataGateway()
    starred_segments = stravaGateway.get_starred_segments()
    gateway = SegmentDataGateway()
    for segment in starred_segments:
        if gateway.get_segment(segment['id']) is None:
            new_segment = Segment(id=segment['id'], name=segment["name"], avg_grade=segment['average_grade'], start_lat=segment['start_latlng'][0], start_long=segment['start_latlng'][1], end_lat=segment['end_latlng'][0], end_long=segment['end_latlng'][1], distance=segment['distance'])
            gateway.insert_segment(new_segment)
    
    segments = gateway.get_all_segments()
    print(segments)
    return "Segment: " + ''.join([f'<p>{segment}</p>' for segment in segments])





