from odoo import models, fields


class Department(models.Model):
    _name = "hda.department"
    name = fields.Char(string='Department Name')
    capacity = fields.Integer(string='Department Capacity')
    opened = fields.Boolean(string='Is Opened')
    pateints_id = fields.One2many(
        'hms.patient', 'departemnt_id', string='Pateints')
