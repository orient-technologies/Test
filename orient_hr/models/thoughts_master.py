# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ThoughtsMaster(models.Model):
    _name = 'thoughts.master'
    _description = 'Thought of the day Master Data'

    name = fields.Char()
    thought_of_day = fields.Text('Thought for the Day')
    today_thought_bool = fields.Boolean(string="Today's Thought?")

    @api.onchange('today_thought_bool')
    def check_today_thought_bool(self):
        """ Author - Rishi Shetty

            code to enforce the selection of only one thought for a particular day
         """
        current_record_today_thought_bool_value = 0
        if self.today_thought_bool:
            current_record_today_thought_bool_value += 1
        else:
            current_record_today_thought_bool_value -= 1
        if (self.env['thoughts.master'].search([('today_thought_bool',
                                                 '=', True)],
                                               count=True) +
                current_record_today_thought_bool_value) > 1:
            raise UserError(_('Cannot set multiple thought of the day,'
                              ' please try resetting the value.'))
