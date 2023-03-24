from odoo import models, fields


class Doctors(models.Model):
    _name = 'hsa.doctors'
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    image = fields.Image()
    major = fields.Char(required=True)
