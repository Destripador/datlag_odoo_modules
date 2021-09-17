# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/archivoRequeridoVacaciones(http.Controller):
#     @http.route('//mnt/extra-addons/archivo_requerido_vacaciones//mnt/extra-addons/archivo_requerido_vacaciones/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/archivo_requerido_vacaciones//mnt/extra-addons/archivo_requerido_vacaciones/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/archivo_requerido_vacaciones.listing', {
#             'root': '//mnt/extra-addons/archivo_requerido_vacaciones//mnt/extra-addons/archivo_requerido_vacaciones',
#             'objects': http.request.env['/mnt/extra-addons/archivo_requerido_vacaciones./mnt/extra-addons/archivo_requerido_vacaciones'].search([]),
#         })

#     @http.route('//mnt/extra-addons/archivo_requerido_vacaciones//mnt/extra-addons/archivo_requerido_vacaciones/objects/<model("/mnt/extra-addons/archivo_requerido_vacaciones./mnt/extra-addons/archivo_requerido_vacaciones"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/archivo_requerido_vacaciones.object', {
#             'object': obj
#         })
