from marshmallow import Schema, fields
class UniversitySchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    type = fields.Str(required=True)
    city = fields.Str(required=True)
    region = fields.Str(required=True)
