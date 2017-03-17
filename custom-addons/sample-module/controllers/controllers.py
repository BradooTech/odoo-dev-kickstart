# -*- coding: utf-8 -*-
from odoo import http

# class Sample-module(http.Controller):
#     @http.route('/sample-module/sample-module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sample-module/sample-module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sample-module.listing', {
#             'root': '/sample-module/sample-module',
#             'objects': http.request.env['sample-module.sample-module'].search([]),
#         })

#     @http.route('/sample-module/sample-module/objects/<model("sample-module.sample-module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sample-module.object', {
#             'object': obj
#         })