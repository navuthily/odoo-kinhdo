from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
class Client(models.Model):
    _name = "client"

    name=fields.Char("Tên khách hàng" , required=True)
    sdt=fields.Char("Số điện thoại")
    dia_chi=fields.Char("Địa chỉ")
    gioi_tinh=fields.Char("Giới tính")
    email=fields.Char("Email")


