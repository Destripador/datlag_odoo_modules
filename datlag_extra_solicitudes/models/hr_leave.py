# -*- coding: utf-8 -*-
from odoo import models, api, fields, _
from odoo.exceptions import ValidationError
import logging
import time

_logger = logging.getLogger(__name__)

class HolidaysRequest(models.Model):
    _inherit = "hr.leave"

    attach_file = fields.Binary()
    attach_file_name = fields.Char()
    attachment_required = fields.Boolean(related='holiday_status_id.attachment_required')

    solicitar_prima = fields.Boolean(related='holiday_status_id.solicitar_prima')
    prima_vacacional = fields.Boolean()
    fecha_solicitud_prima = fields.Date(default=lambda self: fields.datetime.now(), readonly=True)

    #Checar
    @api.onchange('holiday_status_id')
    def _onchange(self):
        for record in self:
            check_prima = self.env['hr.leave'].search([('holiday_status_id','=', record.holiday_status_id.id),('user_id', '=', self.env.uid), ('prima_vacacional', '=', True), ('solicitar_prima', '=', True)], limit=1)
            if check_prima:
                record.solicitar_prima = False

    #Ćhecar que exista un archivo requerido
    @api.constrains('state','holiday_status_id')
    def _check_attachment(self):
        for record in self:
            if record.state not in ['draft', 'cancel', 'refuse'] and record.holiday_status_id.attachment_required:
                if not self.attach_file:
                    raise ValidationError(_('Se necesita un archivo que funcione como justificacion, este archivo sea verificado por los aprovadores'))
                if not self.attach_file_name.endswith(".pdf"):
                    raise ValidationError(_('Necesitas adjuntar documento valido. (PDF o JPG)'))

    #Accion de boton para revocar prima vacacional
    def revocar_prima(self):
        for record in self:
            check_prima = self.env['hr.leave'].search([('holiday_status_id','=', record.holiday_status_id.id),('user_id', '=', record.employee_id.user_id.id), ('prima_vacacional', '=', True), ('solicitar_prima', '=', True)])
            _logger.error("IT IS Error: --" + str(record.holiday_status_id.id))
            for prima in check_prima:
                _logger.error("IT IS Error: " + str(prima))
                prima.prima_vacacional = False
