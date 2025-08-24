from marshmallow import Schema, fields, post_dump
from schemas.base import APIResponse

class ExamGroupCreate(Schema):
    code = fields.String(required=True)
    name = fields.String(required=True)
    subjects = fields.String(required=True)

class ExamGroupUpdate(Schema):
    name = fields.String()
    subjects = fields.String()

class ExamGroupResponse(Schema):
    code = fields.String()
    name = fields.String()
    subjects = fields.String()

    @post_dump
    def strip_fields(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()
        return data
