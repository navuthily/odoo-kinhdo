import math

from odoo import fields, models, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    select_tyle = [
        ('none', ''),
        ('fast', 'Nhanh'),
        ('standard', 'Tiêu chuẩn'),
        ('save', 'Tiết kiệm'),
    ]
    shipper = fields.Many2one("res.partner", string = "Người giao hàng" )
    shipping_type = fields.Selection(select_tyle, string='Phương thức vận chuyển', default=select_tyle[0][0])
