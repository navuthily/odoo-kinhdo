from odoo import fields, models, api,_
from odoo.exceptions import ValidationError


class Product(models.Model):
    _inherit = "product.template"

    loai_hang = fields.Many2one("product.type",string="Loại hàng")
    @api.constrains('default_code')
    def _check_default_codes(self):
        exists = self.env['product.template'].search(
            [('default_code', '=', self.default_code), ('id', '!=', self.id)])
        if exists:
            raise ValidationError(_('Mã sản phẩm ' + self.default_code + ' đã tồn tại.'))