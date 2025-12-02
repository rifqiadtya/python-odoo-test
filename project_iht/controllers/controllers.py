# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectIht(http.Controller):
#     @http.route('/project_iht/project_iht', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_iht/project_iht/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_iht.listing', {
#             'root': '/project_iht/project_iht',
#             'objects': http.request.env['project_iht.project_iht'].search([]),
#         })

#     @http.route('/project_iht/project_iht/objects/<model("project_iht.project_iht"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_iht.object', {
#             'object': obj
#         })

