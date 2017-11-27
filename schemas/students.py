from marshmallow import Schema, fields


class StudentsSchema(Schema):
    # По умолчанию поля name и gender являются обязательными
    field_requirement = True

    def __init__(self, **kwargs):
        field_requirement = kwargs.get('field_requirement')
        if field_requirement:
            self.field_requirement = field_requirement
        super(StudentsSchema, self).__init__(**kwargs)

    birth_date = fields.Str()
    name = fields.Str(required=field_requirement)
    gender = fields.Str(required=field_requirement)
    group_id = fields.Int()
    id = fields.Int()
    phone_number = fields.Str()
