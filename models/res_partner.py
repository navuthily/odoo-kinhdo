# -*- coding: utf-8 -*-

from datetime import timedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    accumulated_point = fields.Integer('Accumulated Point',default=0)
    gender = fields.Selection(string='Giới tính', selection=[('male', 'Nam'), ('female', 'Nữ'), ('none', 'Khác')])
    date_of_birth = fields.Date(string='Ngày sinh')