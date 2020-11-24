# -*- coding: utf-8 -*-
from odoo import http
import datetime
import random
import pytz


class OrientHr(http.Controller):

    @http.route('/home/orient-hr', auth='public', type='http', website=True)
    def custom_homepage_hr(self, **kw):
        """
        This function renders a new custom hompage of the HR module.
        It passes all thoughts for the day records from thoughts.master model
        along with the thought marked as thought for the day. It also returns
        a function which is used to redirect to attendance and employees page
        """
        thought_for_day = http.request.env['thoughts.master'].sudo().search(
            [('today_thought_bool', '=', True)])
        dt = datetime.datetime.now()
        user_tz = http.request.env.user.tz
        local = pytz.timezone(user_tz)
        dt = dt.replace(tzinfo=None)
        current_local_date = pytz.utc.localize(dt).astimezone(local)

        birthdays = http.request.env['hr.employee'].sudo().search([])
        birthday_list_records = []
        for each in birthdays:
            if each.birthday and each.birthday.month == current_local_date.month\
                    and each.birthday.day == current_local_date.day:
                birthday_list_records.append(each)
        redirect_to_colleagues = http.request.env['hr.employee'].sudo().search([
        ], limit=1)
        all_thoughts = http.request.env['thoughts.master'].sudo().search([])
        values = {
            'user': http.request.env.user,
            'thought': thought_for_day,
            'birthdays': birthday_list_records,
            'redirect': redirect_to_colleagues,
            'all_thoughts': all_thoughts
        }

        return http.request.render("orient_hr.orient_hr_homepage_template", values)
