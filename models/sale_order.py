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

    def action_confirm(self):
        for order in self:
            if order.amount_total<1000*order.partner_id.accumulated_point:
                order.amount_total=0
                order.partner_id.accumulated_point -= math.ceil(order.amount_total/1000)
            else:
                order.amount_total -= 1000*order.partner_id.accumulated_point
                order.partner_id.accumulated_point += math.floor(order.amount_total/30000)
        return super(SaleOrder, self).action_confirm()

    def action_done(self):
        super(SaleOrder, self).action_done()
        for order in self:
            order.partner_id.accumulated_point += math.floor(order.amount_total/30000)

    def action_cancel(self):
        super(SaleOrder, self).action_cancel()
        for order in self:
            order.partner_id.accumulated_point += order.accumulated_point
            order.amount_total += 1000*order.accumulated_point
            # order.accumulated_point = 0
