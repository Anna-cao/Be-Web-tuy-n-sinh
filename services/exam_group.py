from models.exam_group import ExamGroup
from database import db

class ExamGroupService:
    @staticmethod
    def get_all():
        return ExamGroup.query.all()

    @staticmethod
    def get_by_id(group_code):
        return ExamGroup.query.get(group_code)

    @staticmethod
    def create(data):
        group = ExamGroup(**data)
        db.session.add(group)
        db.session.commit()
        return group

    @staticmethod
    def update(group_code, data):
        group = ExamGroup.query.get(group_code)
        if group:
            for key, value in data.items():
                setattr(group, key, value)
            db.session.commit()
        return group

    @staticmethod
    def delete(group_code):
        group = ExamGroup.query.get(group_code)
        if group:
            db.session.delete(group)
            db.session.commit()
        return group