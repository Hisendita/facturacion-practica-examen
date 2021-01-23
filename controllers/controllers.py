# -*- coding: utf-8 -*-
# from odoo import http


# class Examen3(http.Controller):
#     @http.route('/examen3/examen3/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/examen3/examen3/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('examen3.listing', {
#             'root': '/examen3/examen3',
#             'objects': http.request.env['examen3.examen3'].search([]),
#         })

#     @http.route('/examen3/examen3/objects/<model("examen3.examen3"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('examen3.object', {
#             'object': obj
#         })
