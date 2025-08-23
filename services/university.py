class CRUDService:
    @staticmethod
    def get_all(model):
        return model.query.all()
    
    @staticmethod
    def get_by_id(model, id):
        return model.query.get_or_404(id)
    
    @staticmethod
    def create(model, data):
        obj = model(**data)
        db.session.add(obj)
        db.session.commit()
        return obj
    
    @staticmethod
    def update(obj, data):
        for k, v in data.items():
            setattr(obj, k, v)
        db.session.commit()
        return obj
    
    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()
        return True
