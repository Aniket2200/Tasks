# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


# class Employee(http.Controller):
#     @http.route('/employee/employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee/employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee.listing', {
#             'root': '/employee/employee',
#             'objects': http.request.env['employee.employee'].search([]),
#         })

#     @http.route('/employee/employee/objects/<model("employee.employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee.object', {
#             'object': obj
#         })


# class NewEmployee(http.Controller):
#     @http.route('/registration', auth='public', website=True)
#     def custom_employee_registration_page(self):
#         customers = request.env['employee.employee_info'].search([])
#         return request.render('employee.employee_registration_template', {'customers': customers})
#
#     @http.route(['/register_submit'], type='http', auth="public", csrf=False, website=True)
#     def website_menu_employee(self, **post):
#         request.env['employee.employee_info'].create(post)
#         return request.render('employee.registration_success_template')

class EmployeeRegistration(http.Controller):
    @http.route(['/registration'], type='http', auth="public", website=True)
    def website_menu(self):
        return request.render("employee.employee_registration_template")

    @http.route(['/register_submit'], type='http', auth="public", website=True)
    def website_menu_employee(self, **post):
        request.env['employee.employee_info'].create(post)
        return request.render('employee.registration_success_template')
