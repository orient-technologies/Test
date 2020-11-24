# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class OrientHR(models.Model):
    _inherit = 'hr.employee'

    def redirect_to_colleagues(self):
        return '%s/web#action=%s&model=%s&view_type=kanban'\
            % (self.env['ir.config_parameter'].sudo().get_param('web.base.url'),
               self.env.ref('hr.open_view_employee_list_my').id, 'hr.employee')

    def redirect_to_attendance(self):
        return '%s/web#action=%s&cids=&menu_id=%s'\
            % (self.env['ir.config_parameter'].sudo().get_param('web.base.url'),
               self.env.ref(
               'hr_attendance.hr_attendance_action_my_attendances').id,
               self.env.ref('hr_attendance.menu_hr_attendance_root').id)


