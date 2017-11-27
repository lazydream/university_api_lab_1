from marshmallow import Schema, fields


class DepartamentsSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    institute = fields.Str()
