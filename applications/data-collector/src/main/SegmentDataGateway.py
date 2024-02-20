from app import db
from SegmentRecord import Segment

class SegmentDataGateway:
    def __init__(self):
        pass

    def get_segment(self, id: int) -> Segment:
        segment = db.session.execute(db.select(Segment).where(Segment.id == id)).one()
        return segment

    def insert_segment(self, segment: Segment) -> None:
        db.session.add(Segment)
        db.session.commit()

