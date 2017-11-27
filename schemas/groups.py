from marshmallow import Schema, fields


class GroupsSchema(Schema):
    name = fields.Str(required=True)
    id = fields.Int()
    departament_id = fields.Int()