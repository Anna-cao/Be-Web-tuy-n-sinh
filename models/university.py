from database import db
from datetime import datetime

class University(db.Model):
    __tablename__ = "universities"

    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50))
    city = db.Column(db.String(100))
    region = db.Column(db.String(50))

    # Relationship
    admission_scores = db.relationship("AdmissionScore", backref="university", lazy=True)

    def __repr__(self):
        return f"<University {self.id} - {self.name}>"
