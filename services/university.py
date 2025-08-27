from database import db

class CRUDService:
    @staticmethod
    def get_all(model):
        return model.query.all()
    
    @staticmethod
    def get_by_id(model, id_value):
        return model.query.get_or_404(id_value)
    
    @staticmethod
    def create(model, data):
        obj = model(**data)
        db.session.add(obj)
        db.session.commit()
        return obj
    
    @staticmethod
    def update(model, id_value, data):
        obj = model.query.get_or_404(id_value)
        for k, v in data.items():
            setattr(obj, k, v)
        db.session.commit()
        return obj
    
    @staticmethod
    def delete(model, id_value):
        obj = model.query.get_or_404(id_value)
        db.session.delete(obj)
        db.session.commit()
        return True