# -*- coding: utf-8 -*-
from openerp import http

# class UsersAdressIp(http.Controller):
#     @http.route('/users_adress_ip/users_adress_ip/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/users_adress_ip/users_adress_ip/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('users_adress_ip.listing', {
#             'root': '/users_adress_ip/users_adress_ip',
#             'objects': http.request.env['users_adress_ip.users_adress_ip'].search([]),
#         })

#     @http.route('/users_adress_ip/users_adress_ip/objects/<model("users_adress_ip.users_adress_ip"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('users_adress_ip.object', {
#             'object': obj
#         })