from odoo import models, fields, api
from datetime import date
import re
from odoo.exceptions import ValidationError


class patient(models.Model):
    _name = 'hsa.patient'

    _sql_constraints = [
        ('email_unique', 'UNIQUE(email)', 'the email address aleardy exists'),
    ]
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
    pcr = fields.Boolean()
    state = fields.Selection([
        ('undetermined', 'Undetermined',),
        ('good,', 'Good,',),
        ('fair,', 'Fair,',),
        ('serious', 'Serious',),
    ])
    departemnt_id = fields.Many2one('hsa.department')
    # doctor = fields.Many2one(comodel_name='hsa.doctors',
    #                          relation='doctor_for_patient')

    doctor = fields.Many2one('hsa.doctors')
    department_capacity = fields.Integer(related='department_id.capacity')
    email = fields.Char(required=True)
    log_id = fields.One2many('hsa.patientLogs', 'patients_id')

    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match(
                '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')

    @api.onchange('state')
    def onchange_state(self):
        """
        Created by, Date, description
        """
        if self.state:
            log_info = f"State has  changed to {self.state}"
            log = self.env['hsa.patient.log'].create({
                'patient_id': self.id,
                'created_by': self.env.user.name,
                'description': log_info
            })
            self.log_id += log

    @api.onchange('age')
    def _age_onchange(self):
        if self.age and self.age < 30:
            self.PCR = True
            return {'warning': {'title': 'PCR Message', 'message': 'pcr is changed to TRUE'}}
        else:
            self.PCR = False
