from marshmallow import Schema, fields


class TeachersSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    gender = fields.Str(required=True)
    birth_date = fields.Str()
    phone_number = fields.Str()
    departament_id = fields.Int()
    course_id = fields.Int()

    # Юзаж в представлении тичера
    departament_name = fields.Str()
    institute = fields.Str()