# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class SaleQuotation(models.Model):
    _name = "sale.quotation"  # <- new model name
    _inherit = "sale.order"  # <- inherit fields and methods from model "my.pet"
    _description = "Prototype inheritance"

    # add new field
    is_super_strength = fields.Boolean("Is Super Strength", default=False)
    is_fly = fields.Boolean("Is Super Strength", default=False)
    planet = fields.Char("Planet")

