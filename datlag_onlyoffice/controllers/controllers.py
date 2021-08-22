# -*- coding: utf-8 -*-
# from odoo import http


# class DatlagOnlyoffice(http.Controller):
#     @http.route('/datlag_onlyoffice/datlag_onlyoffice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/datlag_onlyoffice/datlag_onlyoffice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('datlag_onlyoffice.listing', {
#             'root': '/datlag_onlyoffice/datlag_onlyoffice',
#             'objects': http.request.env['datlag_onlyoffice.datlag_onlyoffice'].search([]),
#         })

#     @http.route('/datlag_onlyoffice/datlag_onlyoffice/objects/<model("datlag_onlyoffice.datlag_onlyoffice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('datlag_onlyoffice.object', {
#             'object': obj
#         })
