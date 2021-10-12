# -*- coding: utf-8 -*-
# from odoo import http


# class GosslerPortal(http.Controller):
#     @http.route('/gossler_portal/gossler_portal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gossler_portal/gossler_portal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gossler_portal.listing', {
#             'root': '/gossler_portal/gossler_portal',
#             'objects': http.request.env['gossler_portal.gossler_portal'].search([]),
#         })

#     @http.route('/gossler_portal/gossler_portal/objects/<model("gossler_portal.gossler_portal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gossler_portal.object', {
#             'object': obj
#         })
