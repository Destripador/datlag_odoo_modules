# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /mnt/extra-addons/archivo_requerido_vacaciones(models.Model):
#     _name = '/mnt/extra-addons/archivo_requerido_vacaciones./mnt/extra-addons/archivo_requerido_vacaciones'
#     _description = '/mnt/extra-addons/archivo_requerido_vacaciones./mnt/extra-addons/archivo_requerido_vacaciones'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
