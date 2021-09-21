# -*- coding: utf-8 -*-
from odoo import models, api, fields, _
from odoo.exceptions import ValidationError

class HolidaysRequest(models.Model):
    _inherit = "hr.leave"

    attach_file = fields.Binary()
    attach_file_name = fields.Char()
    attachment_required = fields.Boolean(related='holiday_status_id.attachment_required')

    @api.constrains('state','holiday_status_id')
    def _check_attachment(self):
        for record in self:
            if record.state not in ['draft', 'cancel', 'refuse'] and record.holiday_status_id.attachment_required:
                #if not self.env['ir.attachment'].search([('res_model','=', self._name), ('res_id','=', record.id)], limit = 1):
                if not self.attach_file:
                    raise ValidationError(_('Se necesita un archivo que funcione como justificacion, este archivo sea verificado por los aprovadores'))
                if not self.attach_file_name.endswith(".pdf"):
                    raise ValidationError(_('Necesitas adjuntar documento valido. (PDF o JPG)'))
