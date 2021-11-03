import math

from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    accumulated_point = fields.Integer()

    def action_done(self):
        super(SaleOrder, self).action_done()
        for order in self:
            order.partner_id.accumulated_point += math.floor((order.amount_total + 1000* order.accumulated_point)/30000)

    def action_cancel(self):
        super(SaleOrder, self).action_cancel()
        for order in self:
            order.partner_id.accumulated_point += order.accumulated_point
            order.amount_total += 1000*order.accumulated_point
            order.accumulated_point = 0
