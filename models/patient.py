from odoo import models, fields


class patient(models.Model):
    _name = 'hsa.patient'
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)

    birth_date = fields.Date(required=True)
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection(selection=[
        ("type a", "A"),
        ("type a+", "A+"),
        ("type b", "B"),
    ])
    image = fields.Image()
    age = fields.Integer(required=True)
    address = fields.Text()
    gender = fields.Selection(selection=[
        ("Femal", "female"),
        ("Male", "male")

    ])
    departemnt_id = fields.Many2one('hsa.department')
