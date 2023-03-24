from odoo import models, fields


class department(models.Model):
    _name = 'hsa.department'
    name = fields.Char(required=True)
    capacity = fields.Integer()
    Is_opened = fields.Boolean()
    # patients = fields.One2many(
    #     "hsa.patient")
