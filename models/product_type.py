from odoo import _, models, fields, api
from odoo.exceptions import ValidationError


class ProductType(models.Model):
    _name = "product.type"
    _description = "Loại hàng"

    product_type_code = fields.Char('Phân khúc', size=128, required=True ,default='')
    name = fields.Char('Tên loại hàng', size=256, required=True)
    description = fields.Char('Diễn giải', size=500, required=False)
    active = fields.Boolean('Có hiệu lực', required=False, default=True)

    def validate_on_save(self):
        exists = self.env['product.type'].search(
            [('product_type_code', '=', self.product_type_code), ('id', '!=', self.id), ('active', 'in', (True, False))])
        if exists:
            raise ValidationError(_('Mã loại hàng ' + self.product_type_code + ' đã tồn tại.'))

    @api.model
    def create(self, vals_list):
        res = super(ProductType, self).create(vals_list)
        res.validate_on_save()
        return res

    def write(self, vals):
        res = super(ProductType, self).write(vals)
        if len(self) == 1:
            self.validate_on_save()
        return res