from marshmallow import Schema, fields, post_dump
from schemas.base import APIResponse

class AdmissionScoreCreate(Schema):
    id = fields.String(required=True)
    major_id = fields.String(required=True)
    group_code = fields.String(required=True)
    year = fields.Integer(required=True)
    score = fields.Float(required=True)

class AdmissionScoreUpdate(Schema):
    major_id = fields.String()
    group_code = fields.String()
    year = fields.Integer()
    score = fields.Float()

class AdmissionScoreResponse(Schema):
    id = fields.String()
    major_id = fields.String()
    group_code = fields.String()
    year = fields.Integer()
    score = fields.Float()

    @post_dump
    def strip_fields(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()
        return data