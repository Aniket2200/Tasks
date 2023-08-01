from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CarEmployee(models.Model):
    _name = 'employee.employee_info'
    _description = 'employee info'

    name = fields.Char(string="First Name")
    last = fields.Char(string="Last Name")
    address = fields.Text(string="Address")
    city = fields.Char(string="City")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Mobile Number")
    state = fields.Selection(
        [('maharashtra', 'Maharashtra'),
         ('delhi', 'Delhi'),
         ('andra_paresh', 'Andra paresh')],
        string='State')

    @api.model
    def create(self, vals):
        # Check if an email with the same value already exists in the database
        if 'email' in vals:
            existing_record = self.env['employee.employee_info'].sudo().search([('email', '=', vals['email'])], limit=1)
            if existing_record:
                raise ValidationError("An entry with the same email already exists.")
        return super(CarEmployee, self).create(vals)
