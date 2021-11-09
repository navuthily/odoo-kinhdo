import math

from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    STATES = [
        ('prepare', 'Chuẩn bị đơn hàng'),
        ('delivering', 'Đang giao'),
        ('delivered', 'Đã giao'),
    ]
    delivery_status = fields.Selection(STATES, string='Trạng thái đơn hàng', default=STATES[0][0])
    delivery_address = fields.Char(string='Địa điểm giao hàng')
    accumulated_point = fields.Integer(compute='_compute_accumulated_point', store=True)

    def action_done(self):
        super(SaleOrder, self).action_done()
        for order in self:
            order.partner_id.accumulated_point += math.floor(order.amount_total/30000)

