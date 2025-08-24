from database import db

class Major(db.Model):
    __tablename__ = "majors"

    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    university_id = db.Column(db.String(10), db.ForeignKey("universities.id"))

    # Relationship
    admission_scores = db.relationship("AdmissionScore", backref="major", lazy=True)

    def __repr__(self):
        return f"<Major {self.id} - {self.name}>"
