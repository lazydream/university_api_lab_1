from marshmallow import Schema, fields


class TeachersSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    gender = fields.Str(required=True)
    birth_date = fields.Str()
    phone_number = fields.Str()
    departament_id = fields.Int(required=True)
    course_id = fields.Int()