from marshmallow import Schema, fields


class StudentSchema(Schema):
    birth_date = fields.Str()
    name = fields.Str()
    gender = fields.Str()
    group_id = fields.Int()
    id = fields.Int()
    phone_number = fields.Str()