import math

from odoo import fields, models, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    shipper = fields.Many2one("res.partner", string = "Người giao hàng" )

