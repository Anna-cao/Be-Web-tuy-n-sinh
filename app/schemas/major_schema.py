from marshmallow import Schema, fields
class MajorSchema(Schema):
    major_id = fields.Str(required=True)
    name = fields.Str(required=True)
    group_major = fields.Str(required=True)
