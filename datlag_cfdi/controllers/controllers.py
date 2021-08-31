# -*- coding: utf-8 -*-
# from odoo import http


# class Datlagcfdi(http.Controller):
#     @http.route('/datlag_cfdi/datlag_cfdi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/datlag_cfdi/datlag_cfdi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('datlag_cfdi.listing', {
#             'root': '/datlag_cfdi/datlag_cfdi',
#             'objects': http.request.env['datlag_cfdi.datlag_cfdi'].search([]),
#         })

#     @http.route('/datlag_cfdi/datlag_cfdi/objects/<model("datlag_cfdi.datlag_cfdi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('datlag_cfdi.object', {
#             'object': obj
#         })
