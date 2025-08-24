from database import db

class ExamGroup(db.Model):
    __tablename__ = "exam_groups"

    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    # Relationship
    admission_scores = db.relationship("AdmissionScore", backref="exam_group", lazy=True)

    def __repr__(self):
        return f"<ExamGroup {self.code} - {self.name}>"
