from marshmallow import Schema, fields

class APIResponse(Schema):
    status = fields.String(required=True)  
    message = fields.String(required=True)  
    data = fields.Raw(required=False)
