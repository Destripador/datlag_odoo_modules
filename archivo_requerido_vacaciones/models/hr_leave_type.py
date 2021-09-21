from odoo import models, fields

class HolidaysType(models.Model):
    _inherit = "hr.leave.type"

    attachment_required = fields.Boolean('Attachment Required')
