from odoo import models, fields


class Logs(models.Model):
    _name = 'hsa.patientLogs'
    _table = 'logs'
    _rec_name = 'description'
    description = fields.Text()
    patient_id = fields.Many2one('hsa.patient')
