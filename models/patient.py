from odoo import models, fields


class patient(models.Model):
    _name = 'hsa.patient'
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    
    birth_date = fields.Date(string="Birth Date", required=True)
    history = fields.Html("your medical history")
    cr_ratio = fields.Float(string="CR Ratio")
    blood_type = fields.Selection(string="Blood Type", selection=[
        ("type a", "A"),
        ("type a+", "A+"),
        ("type b", "B"),
    ])
    image = fields.Image(string="your profile image")
    age = fields.Integer(string="your age", required=True)
    address = fields.Text(string="your address")
