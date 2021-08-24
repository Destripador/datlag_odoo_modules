# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inicio(models.Model):
     _name = 'datlag_onlyoffice.inicio'
     _description = 'modelo de pruba para subida de archivos'

     archivo = fields.Binary()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
