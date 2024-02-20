from app import db
from SegmentRecord import Segment

class SegmentDataGateway:
    def __init__(self):
        db.create_all()

    def get_segment(self, id: int) -> Segment:
        segment = db.session.execute(db.select(Segment).where(Segment.id == id)).first()
        return segment
    
    def get_all_segments(self) -> list[Segment]:
        segments = db.session.execute(db.select(Segment)).all()
        return segments

    def insert_segment(self, segment: Segment) -> None:
        db.session.add(segment)
        db.session.commit()

