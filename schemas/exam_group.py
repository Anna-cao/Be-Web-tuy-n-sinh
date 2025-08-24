from marshmallow import Schema, fields, post_dump
from schemas.base import APIResponse

class ExamGroupCreate(Schema):
    code = fields.String(required=True)  # PK
    name = fields.String(required=True)

class ExamGroupUpdate(Schema):
    name = fields.String()

class ExamGroupResponse(Schema):
    code = fields.String()
    name = fields.String()

    @post_dump
    def strip_fields(self, data, **kwargs):
        for k, v in data.items():
            if isinstance(v, str):
                data[k] = v.strip()
        return data
