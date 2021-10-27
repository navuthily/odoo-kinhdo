from openpyxl.worksheet import related

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    ten_hd=fields.Many2one("contract", required=True , string="Tên hợp đồng")
    so_hd=fields.Char('Số hợp đồng')
    khach_hang=fields.Many2one("client",string="Khách hàng")
    note = fields.Char("Nội dung" )

