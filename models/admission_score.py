from database import db
from datetime import datetime

class AdmissionScore(db.Model):
    __tablename__ = "admission_score"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    university_id = db.Column(db.String(10), db.ForeignKey("universities.id"), nullable=False)
    major_id = db.Column(db.String(10), db.ForeignKey("majors.major_id"), nullable=False)
    group_code = db.Column(db.String(10), db.ForeignKey("exam_groups.group_code"), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    min_score = db.Column(db.Float, nullable=False)
    quota = db.Column(db.Integer, nullable=False)
    note = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<AdmissionScore {self.id} - {self.university_id}/{self.major_id}>"
