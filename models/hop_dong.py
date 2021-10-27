from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class contract(models.Model):
    _name = "contract"
    _description = 'Hợp đồng'

    x_type_contract = fields.Selection([
        ('one', 'Hợp đồng mua'),
        ('true', 'Hợp đồng bán')], string='Loại hợp đồng', required=True, default='true')
    x_number_contract = fields.Char('Số hợp đồng', required=True, default='')
    name = fields.Char('Tên hợp đồng', required=True)
    x_date_start = fields.Date('Ngày ký kết', required=False)
    x_date_end = fields.Date('Ngày kết thúc', required=False)
    x_content = fields.Char('Nội dung', required=False)
    x_currency = fields.Many2one('res.currency', 'Loại tiền',)
    x_client = fields.Many2one( "client",'Khách hàng', required=True,)

    @api.constrains('x_number_contract')
    def _check_default_code(self):
        exists = self.env['contract'].search(
            [('x_number_contract', '=', self.x_number_contract), ('id', '!=', self.id)])
        if exists:
            raise ValidationError(_('Số hợp đồng ' + self.x_number_contract + ' đã tồn tại.'))


