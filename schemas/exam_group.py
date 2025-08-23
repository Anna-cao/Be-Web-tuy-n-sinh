from marshmallow import Schema, fields, post_dump
from schemas.base import APIResponse

class ExamGroupCreate(Schema):
    group_code = fields.String(required=True)
    description = fields.String(required=True)

class ExamGroupUpdate(Schema):
    description = fields.String()

class ExamGroupResponse(Schema):
    group_code = fields.String()
    description = fields.String()

    @post_dump
    def strip_fields(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()
        return data
