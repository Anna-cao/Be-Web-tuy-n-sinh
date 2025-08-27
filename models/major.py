from database import db

class Major(db.Model):
    __tablename__ = "majors"

    major_id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    group_major = db.Column(db.String(100))

    def __repr__(self):
        return f"<Major {self.major_id} - {self.name}>"