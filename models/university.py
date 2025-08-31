
from database import db

class University(db.Model):
    __tablename__ = "universities"

    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    type = db.Column(db.String(50))
    city = db.Column(db.String(100))
    region = db.Column(db.String(50))

    def __repr__(self):
        return f"<University {self.id} - {self.name}>"
