from marshmallow import Schema, fields


class CoursesSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    teacher_id = fields.Int()
    group_id = fields.Int()
    semester = fields.Int()
    duration = fields.Int()
    group_name = fields.Str()
    departament_name = fields.Str()
    institute = fields.Str()
    course = fields.Int(allow_none=True)
    teacher_name = fields.Str()
