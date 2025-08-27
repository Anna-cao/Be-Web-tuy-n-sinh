from database import db

class ExamGroup(db.Model):
    __tablename__ = "exam_groups"

    group_code = db.Column(db.String(10), primary_key=True)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<ExamGroup {self.group_code} - {self.description}>"