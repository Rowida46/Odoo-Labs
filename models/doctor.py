from odoo import models, fields


class Doctors(models.Model):
    _name = 'hms.doctors'
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)

    image = fields.Image(string="your profile image dr")
