from marshmallow import Schema, fields


class IdListSchema(Schema):
    id_list = fields.List(fields.Int())
