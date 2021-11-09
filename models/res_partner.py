# -*- coding: utf-8 -*-

from datetime import timedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'
    type_cus = [('normal','Thường'), ('bronze', 'Đồng'), ('silver', 'Bạc'), ('gold', 'Vàng')]
    type_customer = fields.Selection(type_cus, string='Loại khách hàng',default=type_cus[0][0])
    accumulated_point = fields.Integer('Điểm tích lũy', default=0)
    gender = fields.Selection(string='Giới tính', selection=[('male', 'Nam'), ('female', 'Nữ'), ('none', 'Khác')])
    date_of_birth = fields.Date(string='Ngày sinh')