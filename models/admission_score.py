from database import db
from datetime import datetime

class AdmissionScore(db.Model):
    __tablename__ = "admission_scores"

    id = db.Column(db.String(10), primary_key=True)
    major_id = db.Column(db.String(10), db.ForeignKey("majors.id"), nullable=False)
    group_code = db.Column(db.String(10), db.ForeignKey("exam_groups.code"), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
