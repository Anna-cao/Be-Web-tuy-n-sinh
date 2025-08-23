from marshmallow import Schema, fields, post_dump
from schemas.base import APIResponse

class AdmissionScoreCreate(Schema):
    university_id = fields.String(required=True)
    major_id = fields.String(required=True)
    group_code = fields.String(required=True)
    year = fields.Integer(required=True)
    min_score = fields.Float(required=True)
    quota = fields.Integer(required=True)
    note = fields.String()

class AdmissionScoreUpdate(Schema):
    university_id = fields.String()
    major_id = fields.String()
    group_code = fields.String()
    year = fields.Integer()
    min_score = fields.Float()
    quota = fields.Integer()
    note = fields.String()

class AdmissionScoreResponse(Schema):
    id = fields.Int()
    university_id = fields.String()
    major_id = fields.String()
    group_code = fields.String()
    year = fields.Int()
    min_score = fields.Float()
    quota = fields.Int()
    note = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    @post_dump
    def strip_fields(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()
        return data
