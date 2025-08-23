from database import db

class ExamGroup(db.Model):
    __tablename__ = "exam_groups"

    group_code = db.Column(db.String(10), primary_key=True)
    description = db.Column(db.Text)

    # Relationship
    admission_scores = db.relationship("AdmissionScore", backref="exam_group", lazy=True)

    def __repr__(self):
        return f"<ExamGroup {self.group_code}>"
