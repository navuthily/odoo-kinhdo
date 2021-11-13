# -*- coding: utf-8 -*-

from datetime import timedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'
    type_cus = [('normal','Thường'), ('bronze', 'Đồng'), ('silver', 'Bạc'), ('gold', 'Vàng')]
    accumulated_point = fields.Integer('Điểm tích lũy', default=0)
    gender = fields.Selection(string='Giới tính', selection=[('male', 'Nam'),
                                                             ('female', 'Nữ'), ('none', 'Khác')])
    date_of_birth = fields.Date(string='Ngày sinh')
    type_customer = fields.Char('Loại KH', compute='_compute_type_customer')
    #  type_customer = fields.Selection(type_cus, string='Loại khách hàng', compute='_compute_type_customer')
    @api.depends('total_invoiced')
    def _compute_type_customer(self):
        for rec in self:
            if rec.total_invoiced > 10000000:
                rec.type_customer = 'Vàng'
            if rec.total_invoiced > 5000000:
                rec.type_customer = 'Bạc'
            if rec.total_invoiced > 2000000:
                rec.type_customer = 'Đồng'
            else:
                rec.type_customer = 'Thường'

